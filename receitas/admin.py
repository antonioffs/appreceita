from django.contrib import admin
from .models import Receita


class ListReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo')
    list_display_links = ('id', 'nome_receita', 'categoria', 'tempo_preparo')


# Register your models here.

admin.site.register(Receita, ListReceitas)

