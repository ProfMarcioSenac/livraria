from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo