from django.db import models

class Peliculas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()

class CategoriaCandy(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'


class Candy(models.Model):
    categoria = models.ForeignKey(CategoriaCandy, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
