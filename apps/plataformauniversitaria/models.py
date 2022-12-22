from django.db import models

# Create your models here.
class PLATAFORMAU(models.Model):
    nombre = models.CharField("Nombre",max_length=40)
    descripcion = models.TextField("Descripción")
    url = models.CharField("Url",max_length=40)

    def __str__(self):
        return '%s %s' % (self.nombre)