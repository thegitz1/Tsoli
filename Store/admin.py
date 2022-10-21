from django.contrib import admin
from .models import Produit, Categorie, Commande

admin.site.site_header= "Page d'Administration de TSOLI"
admin.site.site_title= "TSOLI MARKET"
admin.site.index_title= "Manageur"



class AdminCategorie(admin.ModelAdmin):
    list_display= ('name', 'date_added')

class AdminProduit(admin.ModelAdmin):
    list_display= ('titre', 'prix', 'categorie', 'date_added')
    search_fields = ('titre',)
    liste_editable= ('price', )

class AdminCommande(admin.ModelAdmin):
    list_display= ('items', 'nom', 'telephone','adresse', 'ville', 'total')
    search_fields = ('nom',)


admin.site.register(Produit, AdminProduit)
admin.site.register(Categorie, AdminCategorie)
admin.site.register(Commande, AdminCommande)

