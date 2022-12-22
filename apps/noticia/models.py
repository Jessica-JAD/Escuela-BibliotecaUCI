from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField("Título",max_length=40)
    resumen = models.TextField("Resumen")
    texto = models.TextField("Descripción de la noticia")
    autor = models.CharField("Autor",max_length=40)

    def __str__(self):
        return '%s %s' % (self.titulo)