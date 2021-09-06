from django.contrib import admin
from .models import Receita


class ListReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'pessoa', 'publicado')
    list_display_links = ('id', 'nome_receita', 'categoria', 'tempo_preparo')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicado',)
    list_per_page = 5


# Register your models here.

admin.site.register(Receita, ListReceitas)

