from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)
class clientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
