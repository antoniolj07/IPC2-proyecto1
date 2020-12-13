from django.db import models

# Create your models here.
class User(models.Model):
    name  = models.CharField(max_length=120)  # max_length is required in charfileds
    nickname = models.TextField()
    age = models.TextField(blank=True, null=True)  # permite valores nulos
    email = models.CharField(max_length=120)  # valores por default
    dinero = models.DecimalField(decimal_places=2, max_digits=4)  # requeridos