# Generated by Django 5.1.2 on 2024-10-26 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_delete_elemento'),
    ]

    operations = [
        migrations.AddField(
            model_name='agregar',
            name='codigo_qr',
            field=models.ImageField(null=True, upload_to='qr_codes'),
        ),
    ]
