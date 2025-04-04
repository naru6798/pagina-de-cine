from django.urls import path
from candy import views
from django.contrib.auth.views import LogoutView

app_name = 'candy'

urlpatterns = [
    path('', views.index, name='index'),
    path('candy/', views.candy_list, name='candy_list'),
    path('about/', views.about, name='about'),
    path('empleados/', views.empleados, name='empleados'),
    path('candy/update/<int:pk>/', views.candy_update, name='candy_update'),
    path('candy/delete/<int:pk>/', views.candy_delete, name='candy_delete'),
    path('login/', views.MiLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='candy/logout.html'), name='logout'),
    path('register/', views.MiRegisterView.as_view(), name='register'),

]

urlpatterns += [
    path('categorias/', views.empleados_categorias, name='categorias'),
    path('categorias/update/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('categorias/delete/<int:pk>/', views.categoria_delete, name='categoria_delete'),
]

urlpatterns += [
    path('peliculas/', views.empleados_peliculas, name='peliculas'),
    path('peliculas/update/<int:pk>/', views.pelicula_update, name='pelicula_update'),
    path('peliculas/delete/<int:pk>/', views.pelicula_delete, name='pelicula_delete'),
]
