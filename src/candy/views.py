from django.shortcuts import render, redirect
from .models import Candy, Peliculas, CategoriaCandy #Punto para modelos dentro de la misma aplicacion
from . import forms
from django.contrib.auth.views import LoginView
from .forms import LoginForm, RegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages




def index(request):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        pelicula = Peliculas.objects.filter(titulo__icontains = busqueda)
    else:
        pelicula = Peliculas.objects.all().order_by('fecha_lanzamiento')
    context = {'pelicula': pelicula}
    return render(request, 'candy/index.html', context)

def candy_list(request):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        candy = Candy.objects.filter(nombre__icontains = busqueda)
    else:
        candy = Candy.objects.all().order_by('nombre')
    context = {'candy': candy}
    return render(request, 'candy/candy_list.html', context)

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





class MiLoginView(LoginView):
    template_name = 'candy/login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('candy:index')
    
    def form_valid(self, form):
        usuario = form.get_user()
        messages.success(self.request, f'Inicio de sesión exitoso. ¡Bienvenido {usuario.username}!')
        return super().form_valid(form)

class MiRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'candy/register.html'
    success_url = reverse_lazy('candy:login')

    def form_valid(self, form):
        messages.success(self.request, f'Registro exitoso. Inicie sesión aquí abajo.')
        return super().form_valid(form)







# CATEGORIAS. EDITAR Y ELIMINAR

def categorias(request):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        categoria = CategoriaCandy.objects.filter(nombre__icontains = busqueda)
    else:
        categoria = CategoriaCandy.objects.all().order_by('nombre')
    context = {'categoria': categoria}
    return render(request, 'candy/categorias.html', context)

def empleados_categorias(request):
    categoria = CategoriaCandy.objects.all().order_by('nombre')
    if request.method == "GET":
        form = forms.CategoriaForm()
    if request.method == "POST": 
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candy:categorias')
    return render(request, 'candy/categorias.html', {'form': form, 'categoria': categoria})

def categoria_update(request, pk:int):
    query = CategoriaCandy.objects.get(id=pk)
    if request.method == "GET":
        form = forms.CategoriaForm(instance=query)
    if request.method == "POST": 
        form = forms.CategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('candy:categorias')
    return render(request, 'candy/categoria_update.html', {'form': form})

def categoria_delete(request, pk:int):
    query = CategoriaCandy.objects.get(id=pk)
    if request.method == "POST": 
        query.delete()
        return redirect('candy:categorias')
    return render(request, 'candy/categoria_delete.html', {'query': query})






# PELICULAS. EDITAR Y ELIMINAR

def peliculas(request):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        pelicula = Peliculas.objects.filter(nombre__icontains = busqueda)
    else:
        pelicula = Peliculas.objects.all().order_by('fecha_lanzamiento')
    context = {'pelicula': pelicula}
    return render(request, 'candy/peliculas.html', context)

def empleados_peliculas(request):
    peliculas = Peliculas.objects.all().order_by('fecha_lanzamiento')
    if request.method == "GET":
        form = forms.PeliculaForm()
    if request.method == "POST": 
        form = forms.PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candy:peliculas')
    return render(request, 'candy/peliculas.html', {'form': form, 'peliculas': peliculas})

def pelicula_update(request, pk:int):
    query = Peliculas.objects.get(id=pk)
    if request.method == "GET":
        form = forms.PeliculaForm(instance=query)
    if request.method == "POST": 
        form = forms.PeliculaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('candy:peliculas')
    return render(request, 'candy/pelicula_update.html', {'form': form})

def pelicula_delete(request, pk:int):
    query = Peliculas.objects.get(id=pk)
    if request.method == "POST": 
        query.delete()
        return redirect('candy:peliculas')
    return render(request, 'candy/pelicula_delete.html', {'query': query})