from django.contrib import admin
from .models import Boek, Film, FodmapItem


@admin.register(Boek)
class BoekAdmin(admin.ModelAdmin):
    list_display = ['achternaam', 'voornaam', 'titel', 'taal', 'created_at']
    list_filter = ['taal', 'created_at']
    search_fields = ['voornaam', 'achternaam', 'titel', 'beschrijving']
    ordering = ['achternaam', 'voornaam']

    fieldsets = (
        ('Auteur', {
            'fields': ('voornaam', 'achternaam')
        }),
        ('Boek Details', {
            'fields': ('titel', 'beschrijving', 'taal')
        }),
        ('Extra', {
            'fields': ('opmerking',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['titel', 'regisseur', 'jaar', 'taal', 'created_at']
    list_filter = ['taal', 'jaar', 'created_at']
    search_fields = ['titel', 'regisseur', 'schrijver', 'acteurs', 'beschrijving']
    ordering = ['titel']

    fieldsets = (
        ('Film Details', {
            'fields': ('titel', 'jaar', 'taal')
        }),
        ('Crew', {
            'fields': ('regisseur', 'schrijver', 'acteurs')
        }),
        ('Beschrijving', {
            'fields': ('beschrijving',)
        }),
    )


@admin.register(FodmapItem)
class FodmapItemAdmin(admin.ModelAdmin):
    list_display = ['naam', 'categorie', 'groep']
    list_filter = ['categorie', 'groep']
    search_fields = ['naam', 'groep']
    ordering = ['categorie', 'naam']
