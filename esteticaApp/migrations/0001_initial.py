# Generated by Django 4.1.1 on 2022-10-03 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreProd', models.CharField(max_length=100, verbose_name='Nombre_Producto')),
                ('precioProd', models.CharField(max_length=100, verbose_name='Precio_Producto')),
                ('contenido', models.CharField(max_length=15, verbose_name='Contenido_neto')),
                ('descripcionProd', models.CharField(max_length=200, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField(default='')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='esteticaApp.productos')),
            ],
        ),
    ]
