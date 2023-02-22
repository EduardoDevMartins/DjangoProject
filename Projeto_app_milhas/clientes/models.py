from django.db import models
from django.utils import timezone


class Compania(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class origem(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    Nome = models.CharField(max_length=255)
    Telefone = models.CharField(max_length=255)
    Email = models.CharField(max_length=255, blank=True)
    Data_voo = models.DateTimeField(default=timezone.now)
    Ticket_voo = models.CharField(max_length=255)
    Dados_vendedor = models.TextField(blank=True)
    Milheiro = models.CharField(max_length=255, blank=True)
    Login = models.CharField(max_length=255, blank=True)
    Senha = models.CharField(max_length=255, blank=True)
    Compania = models.ForeignKey(Compania, on_delete=models.DO_NOTHING)
    Origem = models.ForeignKey(origem, on_delete=models.DO_NOTHING, default="")
    Ativo = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='foto/%Y/%m/%d')

    def __str__(self):
        return self.Nome
