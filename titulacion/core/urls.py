from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pagina/', views.pagina, name='pagina'),
]
