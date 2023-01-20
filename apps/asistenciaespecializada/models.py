from django.db import models

# Create your models here.
class AsistenciaEspecializada(models.Model):
    tipo = models.CharField(verbose_name='Tipo', max_length=40, choices=(
        ('Tesis','Tesis'),
        ('Posgrado','Posgrado'),
        ('Curso','Curso')
    ), default='1')
    descripcion = models.TextField("Descripción")
    respuesta = models.TextField("Respuesta",null= False)

    def __str__(self):
        return '%s %s' % (self.tipo)