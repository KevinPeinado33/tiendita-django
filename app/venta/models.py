from django.db import models
import uuid

class Venta( models.Model ):
    
    id_venta       = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    id_usuario     = models.IntegerField()
    nombre_cliente = models.CharField(max_length=100)
    fecha          = models.CharField(max_length=200)
    cantidad       = models.CharField(max_length=100)
    total          = models.CharField(max_length=100)

class Detalle( models.Model ):

    id_detalle  = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False) 
    id_venta    = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad    = models.CharField(max_length=100)
    precio      = models.DecimalField(max_digits=5, decimal_places=2)

class Producto( models.Model ):
    id_producto  = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nombre       = models.CharField(max_length=200)
    tipo         = models.CharField(max_length=100)
    precio       = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad     = models.IntegerField(default=0)
    url_producto = models.CharField(max_length=900)    

class Usuario( models.Model ):
    
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nombres    = models.CharField(max_length=200)
    usuario    = models.CharField(max_length=100)
    password   = models.CharField(max_length=100)
    rol        = models.CharField(max_length=100)
