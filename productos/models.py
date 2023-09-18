from django.db import models
from django.core.validators import MinValueValidator
from tipos_productos.models import TipoProducto
from django.utils import timezone

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo_barras = models.PositiveIntegerField(validators=[MinValueValidator(13)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    fecha_caducidad = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    cantidad_inventario = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

