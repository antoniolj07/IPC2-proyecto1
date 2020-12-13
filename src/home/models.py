from django.db import models


# Create your models here.
class Home(models.Model):
    titulo  = models.CharField(max_length=120)  # max_length is required in charfileds
    usuario = models.TextField()
    precio = models.TextField(blank=True, null=True)  # permite valores nulos
    apodo = models.CharField(max_length=15, default='jorgoat')  # valores por default
    dinero = models.DecimalField(decimal_places=2, max_digits=4)  # requeridos
    