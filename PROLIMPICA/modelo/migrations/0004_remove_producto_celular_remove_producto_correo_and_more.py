# Generated by Django 4.0.6 on 2022-08-14 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0003_producto_delete_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='telefono',
        ),
    ]
