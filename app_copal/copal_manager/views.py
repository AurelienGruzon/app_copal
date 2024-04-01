from django.shortcuts import render, redirect
from copal_manager.models import Proprietaire, Contrat, BienImmobilier
from copal_manager.forms import ProprietaireForm, ContratForm, BienImmobilierForm

# Create your views here.
def liste_proprietaires(request):
    proprietaires = Proprietaire.objects.all()
    return render(request, 'copal_manager/liste-proprietaires.html', {'proprietaires': proprietaires})

def create_proprietaire(request):
    if request.method == 'POST':
        form = ProprietaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste-proprietaires')
    else:
        form = ProprietaireForm()
    return render(request, 'copal_manager/create-proprietaire.html', {'form': form})

def detail_proprietaire(request, proprietaire_id):
    proprietaire = Proprietaire.objects.get(id=proprietaire_id)
    contrats = Contrat.objects.filter(proprietaire=proprietaire)
    biens_immobiliers = BienImmobilier.objects.filter(proprietaire=proprietaire)
    context = { 'proprietaire': proprietaire, 'contrats': contrats, 'biens_immobiliers': biens_immobiliers}
    return render(request, 'copal_manager/detail-proprietaire.html', context)


def liste_contrats(request):
    contrats = Contrat.objects.all()
    return render(request, 'copal_manager/liste-contrats.html', {'contrats': contrats})

def create_contrat(request):
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste-contrats')
    else:
        form = ContratForm()
    return render(request, 'copal_manager/create-contrat.html', {'form': form})

def detail_contrat(request, contrat_id):
    contrat = Contrat.objects.get(id=contrat_id)
    return render(request, 'copal_manager/detail-contrat.html', {'contrat': contrat})


def liste_biens_immobiliers(request):
    biens_immobiliers = BienImmobilier.objects.all()
    return render(request, 'copal_manager/liste-biens-immobiliers.html', {'biens_immobiliers': biens_immobiliers})

def create_bien_immobilier(request):
    if request.method == 'POST':
        form = BienImmobilierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste-biens-immobiliers')
    else:
        form = BienImmobilierForm()
    return render(request, 'copal_manager/create-bien-immobilier.html', {'form': form})

def detail_bien_immobilier(request, bien_immobilier_id):
    bien_immobilier = BienImmobilier.objects.get(id=bien_immobilier_id)
    return render(request, 'copal_manager/detail-bien-immobilier.html', {'bien_immobilier': bien_immobilier})
