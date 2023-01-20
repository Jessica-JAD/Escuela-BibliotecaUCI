from urllib import request

from django.db import models

# Create your models here.
from django.shortcuts import render


class Adquisicion(models.Model):
    nombread = models.CharField("Nombre de la adquisición",max_length=40)


    def __str__(self):
        return '%s %s' % (self.nombread)

