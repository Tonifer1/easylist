# Tuodaan tarvittavat moduulit Django-URL-reititystä ja REST Framework -reitittimiä varten
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet # Tuodaan ProductViewSet, joka määrittelee, miten tuotteita käsitellään (CRUD-logiikka)

# Luodaan oletusreititin, joka generoi automaattisesti reitit (URL-polut) ViewSet-luokille
router = DefaultRouter()



# Rekisteröidään CategoryViewSet reitittimeen 'category'-polulla
# - 'categories' määrittää URL-polun, jossa tämä ViewSet on käytettävissä (esim. /api/categories/)
# - basename='category' määrittää, miten reitittimen nimetyt polut rakennetaan (esim. 'category-list' ja 'category-detail')
router.register(r'categories', CategoryViewSet, basename='category')

# Määritellään sovelluksen URL-määritykset
urlpatterns = [
    # Sisällytetään reitittimen automaattisesti generoidut URL-reitit /api/-polun alle
    # - Tämä tarkoittaa, että kaikki reitittimen reitit (kuten /api/categories/) tulevat käyttöön
    path('', include(router.urls, )),
]

