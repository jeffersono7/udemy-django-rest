from django.db import models


class PontoTuristico(models.Model):
    nome = models.CharField(max_lenght=150)
    descricao = models.TextField()
    aprovado = models.BooleanField()

    def __str__(self):
        return self.nome
