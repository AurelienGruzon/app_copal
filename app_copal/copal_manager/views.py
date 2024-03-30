from django.shortcuts import render

# Create your views here.
def list_proprietaires(request):
    proprietaires = Proprietaire.objects.all()
    return render(request, 'list-proprietaires.html', {'proprietaires': proprietaires})

def create_proprietaire(request):
    if request.method == 'POST':
        form = ProprietaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-proprietaires')
    else:
        form = ProprietaireForm()
    return render(request, 'create-proprietaire.html', {'form': form})

def detail_proprietaire(request, proprietaire_id):
    proprietaire = Proprietaire.objects.get(id=proprietaire_id)
    return render(request, 'detail-proprietaire.html', {'proprietaire': proprietaire})


def list_contrats(request):
    contrats = Contrat.objects.all()
    return render(request, 'list-contrats.html', {'contrats': contrats})

def create_contrat(request):
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-contrats')
    else:
        form = ContratForm()
    return render(request, 'create-contrat.html', {'form': form})

def detail_contrat(request, contrat_id):
    contrat = Contrat.objects.get(id=contrat_id)
    return render(request, 'detail-contrat.html', {'contrat': contrat})


def list_biens_immobiliers(request):
    biens_immobiliers = BienImmobilier.objects.all()
    return render(request, 'list-biens-immobiliers.html', {'biens_immobiliers': biens_immobiliers})

def create_bien_immobilier(request):
    if request.method == 'POST':
        form = BienImmobilierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-biens-immobiliers')
    else:
        form = BienImmobilierForm()
    return render(request, 'create-bien-immobilier.html', {'form': form})

def detail_bien_immobilier(request, bien_immobilier_id):
    bien_immobilier = BienImmobilier.objects.get(id=bien_immobilier_id)
    return render(request, 'detail-bien-immobilier.html', {'bien_immobilier': bien_immobilier})
