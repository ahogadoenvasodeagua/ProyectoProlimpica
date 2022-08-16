# Generated by Django 4.0.6 on 2022-08-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_remove_cliente_estadocivil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=70)),
                ('apellidos', models.CharField(max_length=70)),
                ('tipoProduct', models.CharField(choices=[('Materia Prima', 'Materia Prima'), ('Producto de Venta', 'Producto de Venta')], default='Materia Prima', max_length=20)),
                ('correo', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('direccion', models.TextField(default='Dirección', max_length=75)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
