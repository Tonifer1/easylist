from django.contrib import admin
from django.urls import path, include


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Tuodaan JWT-token näkymät
from rest_framework.routers import DefaultRouter

# 1. React pyyntö ohjautuu tähän kirjautuessa:  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
# 2. React pyyntö ohjautuu tähän get products: path('api/products/', include('products.urls')),
#  Tämä tarkoittaa:
#  kaikki osoitteet, jotka alkavat /api/products/, ohjataan products-sovelluksen urls.py-tiedostoon.

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('api/products/', include('products.urls')),  # Products-sovelluksen polut
    path('api/categories/', include('categories.urls')),  # Categories-sovelluksen polut
    path('api/notes/', include('notes.urls')),  # Notes-sovelluksen polut
    path('api/users/', include('users.urls')), # Users -sovelluksen polut


    #JWT Token -reitit
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




