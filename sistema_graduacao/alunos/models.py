from django.db import models
from inicio.models import Modalidade, Plano

class Aluno(models.Model):
    faixa_choices = [
        ('branca', 'Branca'),
        ('cinza', 'Cinza'),
        ('amarelo', 'Amarelo'),
        ('laranja', 'Laranja'),
        ('verde', 'Verde'),
        ('azul', 'Azul'),
        ('roxa', 'Roxa'),
        ('marrom', 'Marrom'),
        ('preta', 'Preta'),
    ]

    matricula = models.AutoField(primary_key=True)
    date_inicio = models.DateField(null=True , blank=True)
    nome = models.CharField(max_length=350)
    idade = models.IntegerField()
    faixa = models.CharField(max_length=20, choices=faixa_choices)
    graus = models.IntegerField(default=0)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT, null=True, blank=True)
    plano = models.ForeignKey(Plano, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.matricula} - {self.nome}'
