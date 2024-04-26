from django.contrib import admin
from .models import Person,identification_types, departments, cities, countries, Students

# Register your models here.

class UserFields(admin.ModelAdmin):
    list_display = ('email', 'password', 'status')

class PersonFields(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'age', 'ident_number')

#admin.site.register(User, UserFields)
admin.site.register(Person, PersonFields)
admin.site.register(Students)
admin.site.register(identification_types)
admin.site.register(departments)
admin.site.register(cities)
admin.site.register(countries)

