from django.db import models

# Create your models here.

class Proprietaire(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    addresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=20)

class Contrat(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    frais_gestion = models.DecimalField(max_digits=10, decimal_places=2)
    # Autres champs pour les détails du contrat

class BienImmobilier(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=20)
    taille = models.DecimalField(max_digits=10, decimal_places=2)
    type_bien = models.CharField(max_length=50)
    # Autres champs pour les détails du bien immobilier
