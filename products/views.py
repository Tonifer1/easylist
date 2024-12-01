from rest_framework.viewsets import ModelViewSet
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
        return queryset # palautetaan suodatettu queryset
            


