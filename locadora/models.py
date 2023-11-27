from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)   
    email = models.CharField(max_length=255)
    cartao = models.CharField(max_length=16)
    cnh = models.CharField(max_length=9, null=True)
    
    def __str__(self):  #definição de função adionada
        return f"{self.nome} - {self.cpf}" 
    

class Carro(models.Model):    
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)    
    ano = models.IntegerField()
    cor = models.CharField(max_length=255)
    portas = models.IntegerField()
    diaria = models.DecimalField(max_digits=8, decimal_places=2)
    placa = models.CharField(max_length=7)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.modelo} - {self.marca}"
    

class Locacao(models.Model):    
    cpf = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    placa = models.ForeignKey(Carro, on_delete=models.PROTECT)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    valorTotal = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.cpf} - {self.placa}"