from rest_framework import serializers # tuodaan serializers-moduuli, jonka avulla voi muuntaa Django-mallit JSON-muotoon ja päinvastoin
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'