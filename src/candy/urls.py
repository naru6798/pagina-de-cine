from django.contrib import admin
from django.urls import path
from candy import views

app_name = 'candy'

urlpatterns = [
    path('', views.index, name='index'),
    path('candy/', views.candy_list, name='candy_list'),
    path('empleados/', views.empleados, name='empleados'),
]