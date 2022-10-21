from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import settings
from Page.views import  index, pagedaccueil_view, contact_view, apropos_view
from Store.views import detail, checkout, confirmation

urlpatterns = [

    path('contact/', contact_view, name='contact'),
    path('apropos/', apropos_view, name='apropos'),
    #    path('produits/', produit_list_view, name='liste-produits'),
    #    path('produit/ajouter/', produit_cree_view, name='ajouter-produit'),
    #    path('produit/<int:id>/delete', produit_delete_view, name='supprimer'),
    path('<int:myid>', detail, name='produit-detail'),
    path('checkout/', checkout, name='checkout'),
    path('confirmation/', confirmation, name='confirmation'),
    path("logout/", LogoutView.as_view(), name="logout"),



    path('', index, name='accueil'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)