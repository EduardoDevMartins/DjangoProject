from django.db import models
from django.utils import timezone


class Status(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Resultado(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    Chamado = models.CharField(max_length=7)   
    Data_atrelamento = models.DateTimeField(default=timezone.now)
    Descricao = models.CharField(max_length=255, blank=True)
    Status_atrelamento = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    Resultado_orçamento = models.ForeignKey(Resultado, on_delete=models.DO_NOTHING, default="")
    Ativo = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='foto/%Y/%m/%d')

    def __str__(self):
        return self.Chamado
