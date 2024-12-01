# Tuodaan tarvittavat moduulit Django-URL-reititystä ja REST Framework -reitittimiä varten
from django.urls import include, path
#from rest_framework import routers
from rest_framework.routers import DefaultRouter
# Luodaan oletusreititin, joka generoi automaattisesti reitit (URL-polut) ViewSet-luokille
#router = routers.DefaultRouter()

# Tuodaan ProductViewSet, joka määrittelee, miten tuotteita käsitellään (CRUD-logiikka)
from .views import NotesViewSet

# Rekisteröidään ProductViewSet reitittimeen 'products'-polulla
# - 'products' määrittää URL-polun, jossa tämä ViewSet on käytettävissä (esim. /api/products/)
# - basename='product' määrittää, miten reitittimen nimetyt polut rakennetaan (esim. 'product-list' ja 'product-detail')
router = DefaultRouter()
router.register(r'notes', NotesViewSet, basename='notes')

# Määritellään sovelluksen URL-määritykset
urlpatterns = [
    # Sisällytetään reitittimen automaattisesti generoidut URL-reitit /api/-polun alle
    # - Tämä tarkoittaa, että kaikki reitittimen reitit (kuten /api/products/) tulevat käyttöön
    path('', include((router.urls, 'notes'))),
]

