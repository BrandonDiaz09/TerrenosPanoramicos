from django import forms
from django.forms import fields

from ventas.models import Inmueble

class OfreceForm(forms.ModelForm):
    pass
    class Meta:
        """ Form Settings"""

        model= Inmueble
        fields = {'user', 'surface',
                    'front','bottom',
                    'price','totalprice', 
                    'description',
                    'photo','regimen_propiedad',
                    'status'}