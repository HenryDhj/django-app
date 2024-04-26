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

class Person(DateTimeModel):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    ident_number = models.CharField(max_length=12, blank=True)
    #id_user = models.ForeignKey('User', on_delete = models.CASCADE, blank=False, null=False, default=1)

class Students(DateTimeModel):
    code = models.CharField(max_length = 100)
    status = models.CharField(max_length = 10)

class identification_types(DateTimeModel):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    descrip = models.CharField(max_length = 10)

class departments(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 10)
    descrip = models.CharField(max_length = 10)


class cities(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 50) 
    descrip = models.CharField(max_length = 10)  


class countries(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length = 50)  
    descrip = models.CharField(max_length = 50)  
    
     
    #def __str__(self):
    #    return f"{self.email} - {self.password}"

