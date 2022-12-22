from django.db import models

# Create your models here.
class BibliografiaEsp(models.Model):
    titulo = models.CharField("Título",max_length=40)
    autor = models.CharField("Autor",max_length=40)
    anno = models.PositiveSmallIntegerField("Año", max_length=4)
    editorial = models.CharField("Editorial",max_length=25)
    ciudad = models.CharField("Ciudad",max_length=25)

    def __str__(self):
        return '%s %s' % (self.titulo)