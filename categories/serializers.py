from rest_framework import serializers # tuodaan serializers-moduuli, jonka avulla voi muuntaa Django-mallit JSON-muotoon ja päinvastoin
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'