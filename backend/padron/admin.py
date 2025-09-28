from django.contrib import admin
from .models import Vivienda, Persona, PersonaVivienda, Vehiculo, Mascota

@admin.register(Vivienda)
class ViviendaAdmin(admin.ModelAdmin):
    list_display = ("numero", "calle", "categoria", "activo", "area_m2")
    search_fields = ("numero", "calle", "categoria")
    list_filter = ("activo", "categoria")

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("apellidos", "nombres", "documento_numero", "email", "estado")
    search_fields = ("nombres", "apellidos", "documento_numero", "email")
    list_filter = ("estado",)

@admin.register(PersonaVivienda)
class PersonaViviendaAdmin(admin.ModelAdmin):
    list_display = ("persona", "vivienda", "rol_en_vivienda", "es_responsable", "fecha_desde", "fecha_hasta")
    search_fields = ("persona__nombres", "persona__apellidos", "vivienda__numero")
    list_filter = ("rol_en_vivienda", "es_responsable")

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("placa", "marca", "modelo", "color", "activo", "persona", "vivienda")
    search_fields = ("placa", "marca", "modelo", "persona__apellidos", "vivienda__numero")
    list_filter = ("activo", "color", "marca")

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "raza", "persona", "vivienda")
    search_fields = ("nombre", "tipo", "raza", "persona__apellidos", "vivienda__numero")
