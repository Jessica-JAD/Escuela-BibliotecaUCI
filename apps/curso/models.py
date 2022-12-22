from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField("Nombre del curso", max_length=40)
    ano = models.IntegerField("Año",max_length=4)
    tema = models.TextField("Tema del curso")

    def __str__(self):
        return '%s %s' % (self.nombre)