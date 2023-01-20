from django.db import models

# Create your models here.
class ConsultaTramite(models.Model):
    nombreusuario = models.CharField("Nombre del usuario",max_length=40)
    descripcion = models.TextField("Descripción")
    respuesta = models.TextField("Respuesta",null= False)

    def __str__(self):
        return '%s %s' % (self.nombreusuario)