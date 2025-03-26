from django.urls import path
from candy import views
from django.contrib.auth.views import LogoutView

app_name = 'candy'

urlpatterns = [
    path('', views.index, name='index'),
    path('candy/', views.candy_list, name='candy_list'),
    path('empleados/', views.empleados, name='empleados'),
    path('candy/update/<int:pk>/', views.candy_update, name='candy_update'),
    path('candy/delete/<int:pk>/', views.candy_delete, name='candy_delete'),
    path('login/', views.MiLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='candy/logout.html'), name='logout')
]