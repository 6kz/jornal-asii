from django.contrib import admin

# Register your models here.
from .models import Artigo, Comentario

admin.site.register(Artigo)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'texto', 'data_criacao')

admin.site.register(Comentario, ComentarioAdmin)