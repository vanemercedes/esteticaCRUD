from django.db import models

# Create your models here.

class Productos(models.Model):
    id_producto=models.BigAutoField(primary_key=True)
    nombreProd=models.CharField('Nombre_Producto', max_length=100)
    precioProd=models.CharField('Precio_Producto', max_length=100)
    contenido=models.CharField('Contenido_neto', max_length=15)
    descripcionProd=models.CharField('Descripción', max_length=200, null=True)

class Ventas(models.Model):
    
    id_venta = models.BigIntegerField(primary_key=True, unique=True)
    fecha = models.DateField()
    cantidad=models.IntegerField(default='')
    producto = models.ForeignKey(Productos, blank=True, null=True, related_name='ventas', on_delete = models.CASCADE)
    