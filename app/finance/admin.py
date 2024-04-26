from django.contrib import admin
from .models import Clientes, Productos, Cliente_Productos, Tipo_Transacciones, Transacciones

# Register your models here.

class ClientesFields(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'CorreoElec', 'Cell')

class ProductosFields(admin.ModelAdmin):
    list_display = ('Nombre_prod','Abreviatura', 'Descrip')

class Cliente_ProductosFields(admin.ModelAdmin):
    list_display = ('id_Cliente', 'id_Producto', 'num_Cuenta')

class Tipo_TransaccionesFields(admin.ModelAdmin):
    list_display = ('Nombre', 'Abreviatura', 'Descrip')

class TransaccionesFields(admin.ModelAdmin):
    list_display = ('id_Cliente_Productos', 'Abreviatura', 'monto','fecha_hora','Tipo_Transacciones','estado')

#admin.site.register(User, UserFields)
admin.site.register(Clientes, ClientesFields)
admin.site.register(Productos, ProductosFields)
admin.site.register(Cliente_Productos, Cliente_ProductosFields)
admin.site.register(Tipo_Transacciones, Tipo_TransaccionesFields)
admin.site.register(Transacciones, TransaccionesFields)


# Register your models here.
