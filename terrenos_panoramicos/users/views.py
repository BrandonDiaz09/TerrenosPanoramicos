from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.
def update_profile(request):
    """
    Update a user's profile
    """
    return render (request, 'users/update_profile.html')

def login_view(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            return redirect('catalogo')
        else:
            return render(request, 'users/login.html', {'error' : 'Usuario o contraseña invalidos'})
    return render(request, 'users/login.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'La contraseña no coincide'})
        
        # EMAIL VALIDATION
        u = User.objects.filter(email=email)
        if u:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'El nombre de usuario ya existe, intente con otro'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = email
        user.save()

        profile = Profile(user=user,
                         last_nameMa= request.POST['last_nameMa'])
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):

    logout(request)
    return redirect('login')