from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])


class Book(models.Model):
    titel = models.CharField(max_length=200)
    voornaam = models.CharField(max_length=200)
    achternaam = models.CharField(max_length=200)
    beschrijving = models.TextField(blank=True)
    taal = models.CharField(max_length=200)

    class Meta:
        ordering = ['achternaam', 'voornaam', 'titel']
    def __str__(self):
        return f"{self.titel} - {self.voornaam} {self.achternaam}"
