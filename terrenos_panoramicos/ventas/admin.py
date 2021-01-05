from django.contrib import admin
from ventas.models import Inmueble

# Register your models here.
@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):

    list_display = ('pk','owner','surface','front', 'bottom')
    list_display_links = ('pk',)
    list_editable = ('owner','surface','front', 'bottom')