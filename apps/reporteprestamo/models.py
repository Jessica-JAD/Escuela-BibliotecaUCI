from django.db import models

# Create your models here.
class ReportePrestamoDocumento(models.Model):
    nombrecliente = models.CharField("Nombre del cliente",max_length=50)
    nombredocumento = models.CharField("Nombre del documento",max_length=40)
    tipoprestamo = models.CharField("Tipo de prestamo",max_length=20)
    fechaprestamo = models.DateField("Fecha de prestamo")
    fecharecogida = models.DateField("Fecha de recogida")

    def __str__(self):
        return '%s %s' % (self.nombrecliente)