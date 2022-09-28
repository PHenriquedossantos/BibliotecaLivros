from django.contrib import admin

from .models import Categoria, Livros

admin.site.register(Livros)
admin.site.register(Categoria)

