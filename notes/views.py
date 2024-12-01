from rest_framework.viewsets import ModelViewSet  # Tuodaan ModelViewSet REST Frameworkista
from .models import Notes  # Tuodaan Notes-malli
from .serializers import NotesSerializer  # Tuodaan NotesSerializer
from rest_framework.permissions import IsAuthenticated  # Tuodaan IsAuthenticated-tarkistus

class NotesViewSet(ModelViewSet):  # Määritellään NotesViewSet-luokka
    permission_classes = [IsAuthenticated]  # Määritellään, että käyttäjän täytyy olla kirjautunut
    queryset = Notes.objects.all()  # Haetaan kaikki Notes-objektit tietokannasta
    serializer_class = NotesSerializer  # Määritellään, että käytetään NotesSerializer-luokkaa

    def perform_create(self, serializer):  # perform_create-metodi luokan sisällä
        serializer.save(user=self.request.user)  # Automaattisesti liitetään kirjautunut käyttäjä


        

        
