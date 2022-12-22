from django.db import models

# Create your models here.
class AsistenciaEspecializada(models.Model):
    tipo = models.CharField("Tipo",max_length=40)
    horario = models.CharField("Horario",max_length=50)

    def __str__(self):
        return '%s %s' % (self.tipo)