from django.db import models

# Create your models here.
class ReportePrestamo(models.Model):
    nombrecliente = models.CharField("Nombre del cliente",max_length=50)
    nombredocumento = models.CharField("Nombre del documento",max_length=40)
    tipoprestamo = models.CharField(verbose_name='Tipo de prestamo', max_length=40, choices=(
        ('Interbibliotecario','Interbibliotecario'),
        ('Individual','Individual')
    ), default='1')
    fechaprestamo = models.DateField("Fecha de prestamo")
    fecharecogida = models.DateField("Fecha de recogida")

    def __str__(self):
        return '%s %s' % (self.nombrecliente)