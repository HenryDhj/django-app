from django.db import models
import datetime

#model.DateTimeField(auto_now=True, null=False) => updated_at
#model.DateTimeField(auto_now_add=True, null=False) => Default now()

# Create your models here.
class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

    class Meta:
        abstract = True

class Clientes(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    CorreoElec = models.CharField(max_length=100, blank=True)
    Cell = models.CharField(max_length=10)
    #id_user = models.ForeignKey('User', on_delete = models.CASCADE, blank=False, null=False, default=1)
class Productos(models.Model):
    Nombre_prod = models.CharField(max_length=20)
    Abreviatura = models.CharField(max_length=20)
    Descrip = models.CharField(max_length=20)

class Cliente_Productos(models.Model):
    id_Cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE, blank=False, null=False)
    id_Producto = models.ForeignKey(Productos, on_delete = models.CASCADE, blank=False, null=False)
    num_Cuenta = models.CharField(max_length=20)

class Tipo_Transacciones(models.Model):
    Nombre = models.CharField(max_length=20)
    Abreviatura = models.CharField(max_length=20)
    Descrip = models.CharField(max_length=20)

class Transacciones(models.Model):
    id_Cliente_Productos = models.ForeignKey(Cliente_Productos, on_delete=models.CASCADE)
    Abreviatura = models.CharField(max_length=10)
    monto = models.IntegerField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    Tipo_Transacciones = models.ForeignKey(Tipo_Transacciones, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)

 
     
    #def __str__(self):
    #    return f"{self.email} - {self.password}"
