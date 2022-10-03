from rest_framework import viewsets

from .models import Productos,Ventas
from .serializers import ProductoSerializer,VentasSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset= Productos.objects.all()
    serializer_class = ProductoSerializer

class VentasViewSet(viewsets.ModelViewSet):
    queryset= Ventas.objects.all()
    serializer_class = VentasSerializer






    
