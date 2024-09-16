from django.db import models

class Projetos(models.Model):
    imagem = models.ImageField(upload_to='projetos')
    titulo = models.CharField(max_length=100, blank=True )
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = "Adicionar Projeto"

    def __str__(self):
        return self.titulo