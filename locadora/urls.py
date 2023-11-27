from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('clientes', views.clientes, name='clientes'),
    path('carros', views.carros, name='carros'),
    path('carros/detalhes/<int:id>', views.carro_detalhes, name='carro_detalhes'),
    path('dashboard', views.dashboard, name='dashboard'),
]