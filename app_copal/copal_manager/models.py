from django.db import models

# Create your models here.

class Proprietaire(models.Model):

    def __str__(self):
        return self.nom + ", " + self.prenom

    CHOICES = [('M', 'Monsieur'),('Mme', 'Madame')]
    civilite = models.CharField(max_length=4, choices=CHOICES, default="M")
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=20)

class Contrat(models.Model):

    def __str__(self):
        return self.numero_contrat + ": " + str(self.proprietaire)
    
    numero_contrat=models.CharField(max_length=5, blank = True)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField(null = True, blank = True)
    frais_gestion = models.DecimalField(max_digits=10, decimal_places=2)
    # Autres champs pour les détails du contrat

class BienImmobilier(models.Model):

    def __str__(self):
        return self.nom + "(" + str(self.proprietaire) + ")"
    
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=20)
    taille = models.DecimalField(max_digits=10, decimal_places=2)
    type_bien = models.CharField(max_length=50)
    # Autres champs pour les détails du bien immobilier
