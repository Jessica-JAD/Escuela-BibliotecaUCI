from django.db import models

# Create your models here.
class Adquisicion(models.Model):
    nombread = models.CharField("Nombre de la adquisición",max_length=40)


    def __str__(self):
        return '%s %s' % (self.nombread)