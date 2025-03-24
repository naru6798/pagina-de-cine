from django.shortcuts import render
from . models import Candy, Peliculas
from django.utils import timezone

def index(request):
    pelicula = Peliculas.objects.all().order_by('fecha_lanzamiento')
    return render(request, 'candy/index.html', {'pelicula': pelicula})

def candy_list(request):
    candy = Candy.objects.all().order_by('nombre')
    return render(request, 'candy/candy_list.html', {'candy': candy})

def empleados(request):
    return render(request, 'candy/empleados.html')

