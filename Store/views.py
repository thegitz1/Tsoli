from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProduitForm, RawProduitForm
from .models import Produit, Commande
from django.http import Http404

def produit_list_view(request):
    queryset = Produit.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "liste.html", context)


def produit_delete_view(request, id):
    obj = get_object_or_404(Produit, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
            'object': obj
        }
    return render(request, "delete.html", context)


#def produit_cree_view(request):
    #    form = ProduitForm(request.POST or None)
    #if form.is_valid():
    #    form.save()
    #form = ProduitForm()
    #context = {
    #        'form': form
    #}
    #return render(request, "produit_cree.html", context)


#def initial_render_date(request):
    initial_data = {
        'title':"Cela est mon magnifique titre"
    }
    obj = Produit.objects.get(id=1)
    form = ProduitForm(request.POST or None, initial=initial_data, instance= obj)
    if form.is_valid():
        form.save()
    context = {
            'form': form
    }
    return render(request, "produit_cree.html", context)


def detail(request, myid):
    product_object = Produit.objects.get(id=myid)
    return render(request, "detail.html", {'product': product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        codepostal = request.POST.get('codepostal')
        com = Commande(items=items, total=total, nom=nom, prenom=prenom, email=email, telephone=telephone, adresse=adresse, ville=ville, pays=pays, codepostal=codepostal)
        com.save()
        return redirect('confirmation')

    return render(request, "checkout.html")

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'confirmation.html', {'name':nom})

#def detail(request, id):
#    obj = Produit.objects.get(id=le_num)
#    obj = get_objects_404(Product, id=le_num)
#    try:
#        obj = Produit.objects.get(id=id)
#    except Produit.DoesNotExist:
#        raise Http404
#    context = {
#            'object': obj
#        }
#    return render(request, "detail.html", context)


#def produit_cree_view(request):
#    my_form = RawProduitForm()
#    if request.method == "POST":
#        my_form = RawProduitForm(request.POST)
#        if my_form.is_valid():
#            #now the data is good
#            print(my_form.cleaned_data)
#            Produit.objects.create(**my_form.cleaned_data)
#        else:
#            print(my_form.errors)
#    context = {
#        "form": my_form
#    }
#    return render(request, "produit_cree.html", context)


#def produit_cree_view(request):
#    if request.method == "POST":
#        mon_new_titre = request.POST.get('titre')
#        print(mon_new_titre)
#         Produit.objects.create(titre=mon_new_titre)
#    context = {}
#    return render(request, "produit_cree.html", context)

