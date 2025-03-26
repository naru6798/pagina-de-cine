from django.shortcuts import render, redirect
from .models import Candy, Peliculas #Punto para modelos dentro de la misma aplicacion
from . import models, forms

def index(request):
    pelicula = Peliculas.objects.all().order_by('fecha_lanzamiento')
    return render(request, 'candy/index.html', {'pelicula': pelicula})

def candy_list(request):
    candy = Candy.objects.all().order_by('nombre')
    return render(request, 'candy/candy_list.html', {'candy': candy})

def empleados(request):
    candy = Candy.objects.all().order_by('nombre')
    if request.method == "GET":
        form = forms.CandyForm()
    if request.method == "POST": 
        form = forms.CandyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candy:empleados')
    return render(request, 'candy/empleados.html', {'form': form, 'candy': candy})

def candy_update(request, pk:int):
    query = Candy.objects.get(id=pk)
    if request.method == "GET":
        form = forms.CandyForm(instance=query)
    if request.method == "POST": 
        form = forms.CandyForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('candy:empleados')
    return render(request, 'candy/candy_update.html', {'form': form})

def candy_delete(request, pk:int):
    query = Candy.objects.get(id=pk)
    if request.method == "POST": 
        query.delete()
        return redirect('candy:empleados')
    return render(request, 'candy/candy_delete.html', {'query': query})


