from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)