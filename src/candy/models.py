from django.db import models

class Peliculas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()

class Candy(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
