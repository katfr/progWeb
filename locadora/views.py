from django.http import HttpResponse
from django.template import loader

from .models import Cliente
from .models import Carro

from django.contrib.auth.decorators import login_required

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

@login_required(login_url="/auth/login")
def clientes(request):         # atualize esta função
    clientes = Cliente.objects.all().values()
    template = loader.get_template('clientes.html')
    context = {
        'clientes': clientes,
    }
    return HttpResponse(template.render(context, request))

def carros(request):
    carros = Carro.objects.all().values()
    template = loader.get_template('carros.html')
    context = {
        'carros': carros,
    }
    return HttpResponse(template.render(context, request))


def carro_detalhes(request, id): 
    carro = Carro.objects.get(id=id)
    template = loader.get_template('carro_detalhes.html')
    context = {
        'carro': carro,
    }
    return HttpResponse(template.render(context, request))
    

@login_required(login_url="/auth/login")
def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())