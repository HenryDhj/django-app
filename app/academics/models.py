from django.db import models

from django.db import models
# Create your models here.
#model.DateTimeField(auto_now = true, null = false ) => update_at
#model.DateTimeField(auto_now_add = true, null = false ) => Defaul now()
#usamos models.Model para usar los timpos de campos ejemplos variables
class User(models.Model):
    #como puedo factorizar los datos en una sola clase 
    email = models.EmailField(null = True, blank = True)
    password = models.CharField(null = True, blank = True)
    status = models.BooleanField(null = True, blank = True, default = True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.email

class Person(models.Model):
    firstname = models.CharField(max_length = 20) 
    lastname = models.CharField(max_length = 20)
    #id_ident_type = models.IntegerField()
    age = models.IntegerField()
    #ident_exp_city = models.IntegerField()
    #address = models.CharField(max_length = 150)
    #mobile = models.CharField(max_length = 50)
    ident_number = models.CharField(max_length = 12, blank = True) # blank = true que acaepte valores null
    #,mid_user = models.IntegerField()
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class Student(models.Model):
    code = models.CharField(max_length = 50) 
    id_person = models.IntegerField()
    status = models.BooleanField(null = True, blank = True, default = True) 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class Identification_type(models.Model):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 100) 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class city(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    id_dept = models.IntegerField() 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class departament(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    id_country = models.IntegerField() 
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)


class country(models.Model):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)  
    descrip = models.CharField(max_length = 10)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)
