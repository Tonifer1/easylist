'''from rest_framework.viewsets import ModelViewSet
 # tuodaan viewset Django rest frameworkista, joka tarjoaa valmiita näkymäsettejä
from .models import Product # tuodaan Product malli
from .serializers import ProductSerializer # tuodaan ProductSerializer sarjoitin
from rest_framework.permissions import IsAuthenticated  # Tuodaan IsAuthenticated-tarkistus

class ProductViewSet(ModelViewSet): # määritellään ProductViewSet-luokka, joka perii viewsets.ModelViewSet-luokan
    serializer_class = ProductSerializer # määritellään serializer_class ProductSerializer-luokaksi
    def get_queryset(self): # määritellään get_queryset-metodi
        queryset = Product.objects.all() # haetaan kaikki Product-objektit tietokannasta
        productname = self.request.query_params.get('productname') # haetaan productname-kyselyparametri pyynnöstä
        if productname is not None: # jos productname ei ole None
            queryset = queryset.filter(product_name=productname) # suodatetaan queryset niin, 
                                    #että se sisältää vain ne objektit, joiden product_name vastaa annettua productname-arvoa
        return queryset # palautetaan suodatettu queryset'''

from .models import Product # tuodaan Product malli
from .serializers import ProductSerializer # tuodaan ProductSerializer sarjoitin
from rest_framework.permissions import IsAuthenticated  # Tuodaan IsAuthenticated-tarkistus
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import AllowAny


class IsAdminOrReadOnlyForDelete(BasePermission):
    """
    Salli GET, POST kaikille kirjautuneille.
    DELETE sallitaan vain admin-käyttäjälle.
    """

    def has_permission(self, request, view):
        # Kaikki kirjautuneet saavat tehdä GET, POST, PUT jne.
        if request.method in SAFE_METHODS or request.method in ['POST', 'PUT', 'PATCH']:
            return request.user.is_authenticated

        # DELETE sallitaan vain admin-käyttäjälle
        if request.method == 'DELETE':
            return request.user.is_staff

        return False


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnlyForDelete]

    def get_queryset(self):
        queryset = Product.objects.all()
        productname = self.request.query_params.get('productname')
        if productname is not None:
            queryset = queryset.filter(product_name=productname)
        return queryset
    
'''
| Koodi           | Selitys                                          |
| --------------- | ------------------------------------------------ |
| ('productname') | URL-parametrin nimi (query string)               |
|   productname   | Python-muuttuja, johon URL-parametri talletetaan |
| `product_name`  | Tietokannan (models.py) kenttä                   |
'''
    
# 4.
'''Koska käytetään ModelViewSet, niin GET /api/products/ automaattisesti kutsuu list()-metodia, joka käyttää get_queryset()-metodia
get_queryset() palauttaa kaikki tuotteet
Jos productname on annettu osoiterivillä query-parametrina, tehdään suodatus
Product jota käytetään querysetin suodattamiseen, on Product-malli, joka on määritelty models.py-tiedostossa ja tuotu import komennolla.
| Kirjoittaja | Funktio                       | Tyyppi                   |
| ----------- | ----------------------------- | ------------------------ |
| DRF         | `get_queryset()`              | built-in                 |
| Oma         | `def get_queryset(self): ...`  | override DRF\:n built-in|


'''

'''
Jos ET käyttäisi ModelViewSetiä vaan tekisit manuaalisesti esim. APIView-pohjalta, silloin kirjoittaisit itse näin:
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

| Paikka             | Kuka tekee `response`-olion?               |
| ------------------ | ------------------------------------------ |
| DRF (ModelViewSet) | DRF automaattisesti                        |
| DRF (APIView)      | Sinä kirjoitat `Response(serializer.data)` |
| React              | Sinä otat vastaan `response`               |


'''

'''class ProductViewSet(ModelViewSet): 
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        queryset = Product.objects.all() 
        productname = self.request.query_params.get('productname') 
        if productname is not None:
            queryset = queryset.filter(product_name=productname) 
        return queryset 

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Product.DoesNotExist:
            raise NotFound("Tuotetta ei löydy.")

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Product.DoesNotExist:
            raise NotFound("Tuotetta ei löydy.")'''


            


