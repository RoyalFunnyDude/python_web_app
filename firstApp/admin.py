from django.contrib import admin
from .models import Person, LoginCredential

# Register your models here.
admin.site.register(Person)
admin.site.register(LoginCredential)
