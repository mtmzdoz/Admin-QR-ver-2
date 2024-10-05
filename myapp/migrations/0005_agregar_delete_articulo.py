# Generated by Django 5.1.1 on 2024-09-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_articulo_imagenes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agregar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('pieza', models.IntegerField(choices=[(0, 'Busto'), (2, 'Pintura'), (3, 'Retrato'), (4, 'Otro')])),
                ('descripcion', models.TextField(max_length=255)),
                ('fecha', models.TextField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Articulo',
        ),
    ]
