from django.db import models

# Create your models here.
class TraduccionDocumento(models.Model):
    nombreusuario = models.CharField("Nombre de usuario",max_length=40)
    adjunto1 = models.FileField("Adjuntar",upload_to='upload/', blank=True,null=True)

    def __str__(self):
        return '%s %s' % (self.nombreusuario)
