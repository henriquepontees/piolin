from django.db import models

class Projetos(models.Model):
    imagem = models.ImageField(upload_to='projetos')
    titulo = models.CharField(max_length=100, blank=True )
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = "Adicionar Projeto"

    def __str__(self):
        return self.titulo

    
class Parceiros(models.Model):
    imagem = models.ImageField(upload_to='parceiros')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    link = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = "Adicionar Parceiro"

    def __str__(self):
        return self.nome
    
class ChavesPix(models.Model):
    qrcode = models.ImageField(upload_to='chavepix')
    chave = models.CharField(max_length=100, blank=True )

    class Meta:
        verbose_name_plural = "Adicionar Chave Pix"

    def __str__(self):
        return self.chave

class Eventos(models.Model):
    data = models.DateField()
    titulo = models.CharField(max_length=100, blank=True )
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.titulo