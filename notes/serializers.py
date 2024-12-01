from rest_framework import serializers # tuodaan serializers-moduuli, jonka avulla voi muuntaa Django-mallit JSON-muotoon ja päinvastoin
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'