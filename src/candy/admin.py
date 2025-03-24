from django.contrib import admin
from . import models

@admin.register(models.Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_lanzamiento')
    search_fields = ('titulo',)
    list_filter = ('fecha_lanzamiento',)
    ordering = ('fecha_lanzamiento',)
    date_hierarchy = 'fecha_lanzamiento'

@admin.register(models.Candy)
class CandyAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)
    list_filter = ('precio',)
    ordering = ('nombre',)
