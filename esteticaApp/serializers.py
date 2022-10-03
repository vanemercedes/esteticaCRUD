from .models import Productos, Ventas
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Productos
        fields = '__all__'

class VentasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ventas
        fields = '__all__'


