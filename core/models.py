from django.db import models


class Boek(models.Model):
    """Model for books."""

    TAAL_CHOICES = [
        ('NL', 'Nederlands'),
        ('ENG', 'English'),
        ('D', 'Deutsch'),
        ('', 'Onbekend'),
    ]

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

    @property
    def auteur(self):
        return f"{self.voornaam} {self.achternaam}"


class Film(models.Model):
    """Model for films."""

    TAAL_CHOICES = [
        ('NL', 'Nederlands'),
        ('ENG', 'English'),
        ('D', 'Deutsch'),
        ('', 'Onbekend'),
    ]

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
    """Model for FODMAP items."""

    CATEGORIE_CHOICES = [
        ('Granen', 'Granen'),
        ('Groente', 'Groente'),
        ('Fruit', 'Fruit'),
        ('Zuivel', 'Zuivel'),
        ('Knollen', 'Knollen'),
        ('Peulvruchten', 'Peulvruchten'),
        ('Noten en zaden', 'Noten en zaden'),
        ('Zoetmiddelen', 'Zoetmiddelen'),
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
