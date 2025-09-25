from rest_framework.viewsets import ModelViewSet# tuodaan viewset Django rest frameworkista, joka tarjoaa valmiita näkymäsettejä
from .models import Category # tuodaan Category malli
from .serializers import CategorySerializer # tuodaan CategorySerializer sarjoitin
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(ModelViewSet): # määritellään CategoryViewSet-luokka, joka perii viewsets.ModelViewSet-luokan
    serializer_class = CategorySerializer # määritellään serializer_class CategorySerializer-luokaksi
    permission_classes = [IsAuthenticated]
    def get_queryset(self): # määritellään get_queryset-metodi
        queryset = Category.objects.all() # haetaan kaikki Product-objektit tietokannasta
        categoryname = self.request.query_params.get('categoryname') # haetaan categoryname-kyselyparametri pyynnöstä
        if categoryname is not None: # jos categoryname ei ole None
            queryset = queryset.filter(category_name=categoryname) # suodatetaan queryset niin, 
                                    #että se sisältää vain ne objektit, joiden category_name vastaa annettua categoryname-arvoa
        return queryset # palautetaan suodatettu queryset
    
   