'''from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Tuodaan JWT-token näkymät

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('api/products/', include('products.urls')),  # Products-sovelluksen polut
    path('api/categories/', include('categories.urls')),  # Categories-sovelluksen polut
    path('api/notes/', include('notes.urls')),  # Notes-sovelluksen polut

    # JWT Token -reitit
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]'''

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.models import User
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

# Luo reititin
router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

# URL-konfiguraatiot
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/notes/', include('notes.urls')),
    path('api/users/', include(router.urls)),  # Lisää käyttäjien päätepiste
]


