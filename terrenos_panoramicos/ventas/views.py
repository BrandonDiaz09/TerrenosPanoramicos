from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Forms
#from ventas.forms import 

# Models
from ventas.models import Inmueble


# class PostsFeedView(LoginRequiredMixin, ListView):
#     """Return all published posts."""

#     template_name = 'posts/feed.html'
#     model = Post
#     ordering = ('-created',)
#     paginate_by = 2
#     context_object_name = 'posts'
# Create your views here.


@login_required
def catalogo_view(request):
    return render(request, 'ventas/catalogo.html')