from django.contrib import admin
from ventas.models import Inmueble

# Register your models here.
@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):

    list_display = ('pk','user','surface','front', 'bottom')
    list_display_links = ('pk',)
    list_editable = ('user','surface','front', 'bottom')