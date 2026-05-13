from django.db import models



class Plano(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R$: {self.valor}"
