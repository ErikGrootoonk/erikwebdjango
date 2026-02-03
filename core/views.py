from django.shortcuts import render
from django.http import JsonResponse
from .models import Boek, Film, FodmapItem


def index(request):
    """Homepage view."""
    return render(request, 'index.html')


def boekenlijst(request):
    """Book list view."""
    return render(request, 'boekenlijst.html')


def filmlijst(request):
    """Film list view."""
    return render(request, 'filmlijst.html')


def fodmaplijst(request):
    """FODMAP list view."""
    return render(request, 'fodmaplijst.html')


def berlijn(request):
    """Berlin page view."""
    return render(request, 'berlijn.html')


def verhalen(request):
    """Stories page view."""
    return render(request, 'verhalen.html')


def de_groene_zon(request):
    """De Groene Zon page view."""
    return render(request, 'de_groene_zon.html')


def weird(request):
    """Weird page view."""
    return render(request, 'weird.html')


# API endpoints for JSON data
def api_boeken(request):
    """API endpoint for books data."""
    query = request.GET.get('q', '').lower()
    boeken = Boek.objects.all()

    if query:
        boeken = boeken.filter(
            models.Q(voornaam__icontains=query) |
            models.Q(achternaam__icontains=query) |
            models.Q(titel__icontains=query) |
            models.Q(beschrijving__icontains=query)
        )

    data = list(boeken.values(
        'voornaam', 'achternaam', 'titel', 'beschrijving', 'taal', 'opmerking'
    ))

    # Rename 'taal' to 'Taal' for consistency with original JSON
    for item in data:
        item['Taal'] = item.pop('taal')
        if item['opmerking']:
            item['Opmerking'] = item.pop('opmerking')
        else:
            del item['opmerking']

    return JsonResponse(data, safe=False)


def api_films(request):
    """API endpoint for films data."""
    query = request.GET.get('q', '').lower()
    films = Film.objects.all()

    if query:
        from django.db.models import Q
        films = films.filter(
            Q(titel__icontains=query) |
            Q(regisseur__icontains=query) |
            Q(beschrijving__icontains=query)
        )

    data = list(films.values(
        'titel', 'regisseur', 'schrijver', 'acteurs', 'jaar', 'beschrijving', 'taal'
    ))

    # Rename fields for consistency
    for item in data:
        item['Taal'] = item.pop('taal')

    return JsonResponse(data, safe=False)


def api_fodmap(request):
    """API endpoint for FODMAP data."""
    query = request.GET.get('q', '').lower()
    items = FodmapItem.objects.all()

    if query:
        from django.db.models import Q
        items = items.filter(
            Q(naam__icontains=query) |
            Q(categorie__icontains=query) |
            Q(groep__icontains=query)
        )

    data = []
    for item in items:
        data.append({
            item.categorie: item.naam,
            'groep': item.groep
        })

    return JsonResponse(data, safe=False)
