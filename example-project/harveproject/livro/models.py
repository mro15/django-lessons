from django.db import models


class Livro(models.Model):
    nome = models.CharField(max_length=200)
    nome_autor = models.CharField(max_length=200)
    paginas = models.IntegerField()
