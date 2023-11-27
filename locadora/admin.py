from django.contrib import admin
from .models import Cliente
from .models import Carro
from .models import Locacao

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "email", "cartao","cnh")

class CarroAdmin(admin.ModelAdmin): 
    list_display = ("modelo", "marca", "ano", "cor", "portas", "diaria", "placa", "disponivel", "imagem")


class LocacaoAdmin(admin.ModelAdmin):  
    list_display = ("cpf", "placa", "dataInicio", "dataFim","valorTotal")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Carro, CarroAdmin)
admin.site.register(Locacao, LocacaoAdmin)