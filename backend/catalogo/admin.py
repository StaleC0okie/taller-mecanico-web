from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "activo", "creado_en")
    list_filter = ("activo",) 
    search_fields = ("nombre",) 