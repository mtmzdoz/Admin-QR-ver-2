# Generated by Django 5.1.2 on 2024-10-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_agregar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregar',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='media/imagenes'),
        ),
    ]
