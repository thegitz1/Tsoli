from django.shortcuts import render
from Store.models import Produit, Booking
from django.core.paginator import Paginator


def index(request):
    product_object = Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Produit.objects.filter(titre__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'index.html', {'product_object': product_object})




def pagedaccueil_view(request, *args, **kwargs):
    obj = Produit.objects.all()
    return render(request, 'index.html', {'object': obj})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def apropos_view(request, *args, **kwargs):
    my_context= {
        "my_text": "A propos de nous",
        "mon_numero": 24104141012,
    }
    return render(request, 'apropos.html', my_context)


#def search(request):
#    query = request.GET.get('query')
#    if not query:
#        produits = [
#            produit for produit in Produit
#            if query in " ".join(artist['name'] for artist in album[])
#        ]