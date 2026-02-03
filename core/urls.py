from django.urls import path
from . import views

urlpatterns = [
    # Page views
    path('', views.index, name='index'),
    path('boeken/', views.boekenlijst, name='boekenlijst'),
    path('films/', views.filmlijst, name='filmlijst'),
    path('fodmap/', views.fodmaplijst, name='fodmaplijst'),
    path('berlijn/', views.berlijn, name='berlijn'),
    path('verhalen/', views.verhalen, name='verhalen'),
    path('de-groene-zon/', views.de_groene_zon, name='de_groene_zon'),
    path('weird/', views.weird, name='weird'),

    # API endpoints
    path('api/boeken/', views.api_boeken, name='api_boeken'),
    path('api/films/', views.api_films, name='api_films'),
    path('api/fodmap/', views.api_fodmap, name='api_fodmap'),
]
