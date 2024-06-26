from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pagina/', views.pagina, name='pagina'),
    path('detalles/', views.detalles, name='detalles'),   
    path('login/', views.login, name='login'),   
    path('formulario/', views.formulario, name="formulario")
]
