from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artigo/<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('artigo/<int:artigo_id>/comentarios/', views.pagina_comentarios, name='pagina_comentarios'),
]