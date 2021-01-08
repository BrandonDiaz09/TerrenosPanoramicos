from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    last_nameMa = forms.CharField( min_length=2, max_length=50)
    
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El usuario ya esta en uso')
        return username

    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('El email ya esta en uso')
        return email

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('La contraseña no coincide')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data

        user = User.objects.create_user(username=data['username'], 
                                        password=data['password'],
                                        first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email'])
        profile = Profile(user=user,
                          last_nameMa= data['last_nameMa'])
        profile.save()

class ProfileForm(forms.Form):
    """Profile form."""

    curp = forms.CharField(max_length=18,required=True )
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
    ine = forms.ImageField()