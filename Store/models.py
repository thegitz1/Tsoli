from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.name}'

class Client(models.Model):
    nom = models.CharField(max_length=100, unique=True, null=True)
    localisation = models.URLField(null=True)
    telephone = models.TextField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return f'({self.nom})'

class Commercant(models.Model):
    nom = models.CharField(max_length=100, unique=True, null=True)
    localisation = models.URLField(null=True)
    telephone = models.TextField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return f'({self.id})({self.titre})({self.stock})'

class Produit(models.Model):
    titre = models.TextField(max_length=50, unique=True, null=True)
    prix = models.FloatField(null=True)
    disponbile = models.BooleanField(default=True)
    description = models.TextField(default=f'Description du produit', null=True)
    stock = models.IntegerField(blank=False, null=True)
    thumbnail = models.ImageField(upload_to="models", blank=True, null=True)
    slug = models.SlugField(max_length=120, null=True)
    categorie = ForeignKey(Categorie, related_name='category', on_delete=models.CASCADE, null=True)
    commercant = models.ManyToManyField(Commercant, related_name='produitachete', blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        ordering = ['-date_added']


    def get_absolute_url(self):
        return reverse('produit-detail', kwargs={"id": self.id})


    def __str__(self):
        return f'{self.id} {self.titre} ({self.stock})'


class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=9)
    adresse = models.CharField(max_length=200)
    ville = models.TextField(max_length=60)
    pays = models.CharField(max_length=60)
    codepostal = models.CharField(max_length=5, null=True)
    date_commande = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return f'{self.id} {self.prenom} {self.telephone} ({self.email})'


class Booking(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(null=False)
    contact = ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f'(Commande 00{self.id})'