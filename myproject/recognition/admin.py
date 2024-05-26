from django.contrib import admin
from .models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_carrera', 'imagen')
    search_fields = ('nombre', 'codigo_carrera')

admin.site.register(Alumno, AlumnoAdmin)

