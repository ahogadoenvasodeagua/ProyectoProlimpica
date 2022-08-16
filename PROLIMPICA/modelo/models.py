from datetime import date
from django.db import models

# Create your models here.
class Producto(models.Model):
    listatipoproduct=(
        ('Materia Prima', 'Materia Prima'),
        ('Producto de Venta', 'Producto de Venta'),
    )
    listamarca=(
        ('Tips','Tips'),
        ('MisterMusculo','MisterMusculo'),
        ('Otros','Otros'),
    )
    
    cliente_id = models.AutoField(primary_key = True)
    id = models.CharField(max_length=10, null = False)
    nombres = models.CharField(max_length=70, null = False)
    precio = models.CharField(max_length=6, null = False, default="s/n")
    tipoProduct = models.CharField(max_length=20, choices = listatipoproduct, null = False, default="Materia Prima")
    marca = models.CharField(max_length=20, choices = listamarca, null = False, default="Marcas")
    fechaCaducidad = models.CharField(max_length=70, null = False, default="s/n")
    
    
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.id