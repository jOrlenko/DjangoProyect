# Generated by Django 4.2.7 on 2023-11-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiciosApp', '0002_servicio_created_servicio_detalle_servicio_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios/imagenes'),
        ),
    ]
