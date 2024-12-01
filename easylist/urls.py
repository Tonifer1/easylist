from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('api/products/', include('products.urls')),  # Products-sovelluksen polut
    path('api/categories/', include('categories.urls')),  # Categories-sovelluksen polut
    path('api/users/', include('users.urls')),  # Users-sovelluksen polut
    path('api/notes/', include('notes.urls')),  # Notes-sovelluksen polut
]

