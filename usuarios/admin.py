from django.contrib import admin
from .models import Usuario

# Register your models here.

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 15




admin.site.register(Usuario, ListandoUsuarios)