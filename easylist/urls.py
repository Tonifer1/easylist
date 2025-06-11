from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Tuodaan JWT-token näkymät
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer


# Serializer käyttäjien tiedoille
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# ViewSet käyttäjien listaukseen
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 1. React pyyntö ohjautuu tähän

# Luo reititin
router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('api/products/', include('products.urls')),  # Products-sovelluksen polut
    path('api/categories/', include('categories.urls')),  # Categories-sovelluksen polut
    path('api/notes/', include('notes.urls')),  # Notes-sovelluksen polut

    #JWT Token -reitit
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




