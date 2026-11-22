from django.contrib import admin
from .models import SolicitudContacto

@admin.register(SolicitudContacto)
class SolicitudContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_envio')
    search_fields = ('nombre', 'email')
# Register your models here.
