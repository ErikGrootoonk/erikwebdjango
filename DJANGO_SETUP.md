Here's a complete condensed reference document you can save:

# ErikWeb Django Project - Complete Setup Reference

## Project Structure


erikweb_django/
├── manage.py
├── db.sqlite3
├── erikweb/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── core/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── management/
│ ├── init.py
│ └── commands/
│ ├── init.py
│ └── import_data.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── boekenlijst.html
│ ├── filmlijst.html
│ ├── fodmaplijst.html
│ ├── berlijn.html
│ ├── verhalen.html
│ └── weird.html
└── static/
└── img/
└── sbahn.jpg

---

## Quick Setup Commands


bash

1. Create project directory and virtual environment
mkdir erikweb_django && cd erikweb_django
python -m venv venv
source venv/bin/activate
pip install django

2. Create Django project and app
django-admin startproject erikweb .
python manage.py startapp core

3. Create folder structure
mkdir -p templates static/img
mkdir -p core/management/commands
touch core/management/init.py
touch core/management/commands/init.py

4. Copy image
cp /home/erik/git/erikweb/img/sbahn.jpg static/img/

5. After adding all files, run migrations
python manage.py makemigrations
python manage.py migrate

6. Import existing data
python manage.py import_data \
--boeken /home/erik/git/erikweb/boekenlijst.json \
--films /home/erik/git/erikweb/filmlijst.json \
--fodmap /home/erik/git/erikweb/fodmaplijst.json

7. Create admin user
python manage.py createsuperuser

8. Run server
python manage.py runserver

---

## URLs

- Homepage: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/
- Boeken: http://127.0.0.1:8000/boeken/
- Films: http://127.0.0.1:8000/films/
- FODMAP: http://127.0.0.1:8000/fodmap/

---

## File Contents

### erikweb/settings.py


python
from pathlib import Path

BASE_DIR = Path(file).resolve().parent.parent
SECRET_KEY = 'django-insecure-change-this-in-production'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'core',
]

MIDDLEWARE = [
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'erikweb.urls'

TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [BASE_DIR / 'templates'],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
},
},
]

WSGI_APPLICATION = 'erikweb.wsgi.application'

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}

LANGUAGE_CODE = 'nl'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

---

### erikweb/urls.py


python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('core.urls')),
]

---

### core/models.py


python
from django.db import models

class Boek(models.Model):
TAAL_CHOICES = [('NL', 'Nederlands'), ('ENG', 'English'), ('D', 'Deutsch'), ('', 'Onbekend')]

voornaam = models.CharField(max_length=100, verbose_name="Voornaam auteur")
achternaam = models.CharField(max_length=100, verbose_name="Achternaam auteur")
titel = models.CharField(max_length=255, verbose_name="Titel")
beschrijving = models.TextField(blank=True, verbose_name="Beschrijving")
taal = models.CharField(max_length=10, choices=TAAL_CHOICES, blank=True, verbose_name="Taal")
opmerking = models.TextField(blank=True, verbose_name="Opmerking")
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

class Meta:
    verbose_name = "Boek"
    verbose_name_plural = "Boeken"
    ordering = ['achternaam', 'voornaam', 'titel']

def __str__(self):
    return f"{self.achternaam}, {self.voornaam} - {self.titel}"


class Film(models.Model):
TAAL_CHOICES = [('NL', 'Nederlands'), ('ENG', 'English'), ('D', 'Deutsch'), ('', 'Onbekend')]

titel = models.CharField(max_length=255, verbose_name="Titel")
regisseur = models.CharField(max_length=200, verbose_name="Regisseur")
schrijver = models.CharField(max_length=200, blank=True, verbose_name="Schrijver")
acteurs = models.TextField(blank=True, verbose_name="Acteurs")
jaar = models.CharField(max_length=10, blank=True, verbose_name="Jaar")
beschrijving = models.TextField(blank=True, verbose_name="Beschrijving")
taal = models.CharField(max_length=10, choices=TAAL_CHOICES, blank=True, verbose_name="Taal")
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

class Meta:
    verbose_name = "Film"
    verbose_name_plural = "Films"
    ordering = ['titel']

def __str__(self):
    return f"{self.titel} ({self.jaar})"


class FodmapItem(models.Model):
CATEGORIE_CHOICES = [
('Granen', 'Granen'), ('Groente', 'Groente'), ('Fruit', 'Fruit'),
('Zuivel', 'Zuivel'), ('Knollen', 'Knollen'), ('Peulvruchten', 'Peulvruchten'),
('Noten en zaden', 'Noten en zaden'), ('Zoetmiddelen', 'Zoetmiddelen'),
('Kruiden en specerijen', 'Kruiden en specerijen'),
]

categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES, verbose_name="Categorie")
naam = models.CharField(max_length=200, verbose_name="Naam")
groep = models.CharField(max_length=200, verbose_name="FODMAP Groep")
created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = "FODMAP Item"
    verbose_name_plural = "FODMAP Items"
    ordering = ['categorie', 'naam']

def __str__(self):
    return f"{self.naam} ({self.categorie})"


---

### core/admin.py


python
from django.contrib import admin
from .models import Boek, Film, FodmapItem

@admin.register(Boek)
class BoekAdmin(admin.ModelAdmin):
list_display = ['achternaam', 'voornaam', 'titel', 'taal', 'created_at']
list_filter = ['taal', 'created_at']
search_fields = ['voornaam', 'achternaam', 'titel', 'beschrijving']
ordering = ['achternaam', 'voornaam']

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
list_display = ['titel', 'regisseur', 'jaar', 'taal', 'created_at']
list_filter = ['taal', 'jaar', 'created_at']
search_fields = ['titel', 'regisseur', 'schrijver', 'acteurs', 'beschrijving']

@admin.register(FodmapItem)
class FodmapItemAdmin(admin.ModelAdmin):
list_display = ['naam', 'categorie', 'groep']
list_filter = ['categorie', 'groep']
search_fields = ['naam', 'groep']

---

### core/views.py


python
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import Boek, Film, FodmapItem

def index(request):
return render(request, 'index.html')

def boekenlijst(request):
return render(request, 'boekenlijst.html')

def filmlijst(request):
return render(request, 'filmlijst.html')

def fodmaplijst(request):
return render(request, 'fodmaplijst.html')

def berlijn(request):
return render(request, 'berlijn.html')

def verhalen(request):
return render(request, 'verhalen.html')

def weird(request):
return render(request, 'weird.html')

def api_boeken(request):
boeken = Boek.objects.all()
data = list(boeken.values('voornaam', 'achternaam', 'titel', 'beschrijving', 'taal', 'opmerking'))
for item in data:
item['Taal'] = item.pop('taal')
if not item['opmerking']:
del item['opmerking']
else:
item['Opmerking'] = item.pop('opmerking')
return JsonResponse(data, safe=False)

def api_films(request):
films = Film.objects.all()
data = list(films.values('titel', 'regisseur', 'schrijver', 'acteurs', 'jaar', 'beschrijving', 'taal'))
for item in data:
item['Taal'] = item.pop('taal')
return JsonResponse(data, safe=False)

def api_fodmap(request):
items = FodmapItem.objects.all()
data = [{item.categorie: item.naam, 'groep': item.groep} for item in items]
return JsonResponse(data, safe=False)

---

### core/urls.py


python
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('boeken/', views.boekenlijst, name='boekenlijst'),
path('films/', views.filmlijst, name='filmlijst'),
path('fodmap/', views.fodmaplijst, name='fodmaplijst'),
path('berlijn/', views.berlijn, name='berlijn'),
path('verhalen/', views.verhalen, name='verhalen'),
path('weird/', views.weird, name='weird'),
path('api/boeken/', views.api_boeken, name='api_boeken'),
path('api/films/', views.api_films, name='api_films'),
path('api/fodmap/', views.api_fodmap, name='api_fodmap'),
]

---

### core/management/commands/import_data.py


python
import json
from django.core.management.base import BaseCommand
from core.models import Boek, Film, FodmapItem

class Command(BaseCommand):
help = 'Import data from JSON files'

def add_arguments(self, parser):
    parser.add_argument('--boeken', type=str)
    parser.add_argument('--films', type=str)
    parser.add_argument('--fodmap', type=str)

def handle(self, *args, **options):
    if options['boeken']:
        with open(options['boeken'], 'r', encoding='utf-8') as f:
            for item in json.load(f):
                Boek.objects.get_or_create(
                    voornaam=item.get('voornaam', ''),
                    achternaam=item.get('achternaam', ''),
                    titel=item.get('titel', ''),
                    defaults={
                        'beschrijving': item.get('beschrijving', ''),
                        'taal': item.get('Taal', ''),
                        'opmerking': item.get('Opmerking', ''),
                    }
                )
        self.stdout.write(self.style.SUCCESS('Books imported!'))

    if options['films']:
        with open(options['films'], 'r', encoding='utf-8') as f:
            for item in json.load(f):
                Film.objects.get_or_create(
                    titel=item.get('titel', ''),
                    defaults={
                        'regisseur': item.get('regiseur', item.get('regisseur', '')),
                        'schrijver': item.get('schrijver', ''),
                        'acteurs': item.get('acteurs', ''),
                        'jaar': item.get('jaar', ''),
                        'beschrijving': item.get('beschrijving', ''),
                        'taal': item.get('Taal', ''),
                    }
                )
        self.stdout.write(self.style.SUCCESS('Films imported!'))

    if options['fodmap']:
        with open(options['fodmap'], 'r', encoding='utf-8') as f:
            for item in json.load(f):
                for key, value in item.items():
                    if key != 'groep':
                        FodmapItem.objects.get_or_create(
                            categorie=key, naam=value,
                            defaults={'groep': item.get('groep', '')}
                        )
                        break
        self.stdout.write(self.style.SUCCESS('FODMAP items imported!'))



---

### templates/base.html


html
{% load static %}


Home Berlijn Boeken Film FODMAPlijst Verhalen Weird
{% block content %}{% endblock %} {% block scripts %}{% endblock %}
---

### templates/index.html


html
{% extends 'base.html' %}
{% load static %}

{% block title %}Home - erikweb{% endblock %}

{% block content %}

Welkom op ErikWeb

Dit is een persoonlijk blog over de dingen die me bezighouden

FODMAP beperkt dieet

Ik heb onlangs het FODMAP beperkt dieet gevolgd, om te bepalen waar mijn darmklachten en buikpijn vandaan komt. Dit was een openbaring, omdat ik heel mijn leven allerlei klachten van het bovenstaande had. Al na een paar dagen was het effect merkbaar.

Haruki Murakami

De laatste tijd ben ik veel aan het lezen van Haruki Murakami. Kijk voor boeken die ik de laatste tijd gelezen heb op pagina boeken

S-Bahn
{% endblock %}

---

### templates/boekenlijst.html


html
{% extends 'base.html' %}
{% block title %}Boekenlijst - erikweb{% endblock %}

{% block content %}

Zoeken...
{% endblock %}

{% block scripts %}

{% endblock %}

---

### templates/filmlijst.html


html
{% extends 'base.html' %}
{% block title %}Filmlijst - erikweb{% endblock %}

{% block content %}

Zoeken...
{% endblock %}

{% block scripts %}

{% endblock %}

---

### templates/fodmaplijst.html


html
{% extends 'base.html' %}
{% block title %}FODMAP Lijst - erikweb{% endblock %}

{% block content %}

Zoeken...
{% endblock %}

{% block scripts %}

{% endblock %}

---

### templates/berlijn.html (placeholder)


html
{% extends 'base.html' %}
{% block title %}Berlijn - erikweb{% endblock %}
{% block content %}

Berlijn
Content voor Berlijn pagina...

{% endblock %}

### templates/verhalen.html & templates/weird.html

Same structure as berlijn.html, just change title and heading.

---

## Common Commands Reference


bash

Activate venv
source venv/bin/activate

Run server
python manage.py runserver

Make migrations after model changes
python manage.py makemigrations
python manage.py migrate

Create superuser
python manage.py createsuperuser

Django shell
python manage.py shell

Collect static files (for production)
python manage.py collectstatic

---

## Troubleshooting

**import_data command not found:**


bash
mkdir -p core/management/commands
touch core/management/init.py
touch core/management/commands/init.py

**Static files not loading:**
- Check `STATICFILES_DIRS` in settings.py
- Make sure `{% load static %}` is in template

**Template not found:**
- Check `TEMPLATES['DIRS']` in settings.py
- Verify template file exists in `templates/` folder


Save this file
Run this command to save:

cat > ~/git/erikweb_django/DJANGO_SETUP.md << 'ENDOFFILE'
# Paste all the content above here
ENDOFFILE


Or simply copy everything above and save it manually to ~/git/erikweb_django/DJANGO_SETUP.md.

Good luck with your Django project! 🚀