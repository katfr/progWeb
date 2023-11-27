from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('locadora.urls')),
    path('auth/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]