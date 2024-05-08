from django.db import models

# Create your models here.


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tfno=models.CharField(max_length=7)
    clave = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)

class Articulos(models.Model):

    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField


    class Pedidos(models.Model):

        numero=models.BigIntegerField()
        fecha=models.DateField()
        entregado=models.BooleanField
        