# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario
from .forms import ComentarioForm

def pagina_comentarios(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all() # Vai buscar todos os comentários deste artigo

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo # Associa o comentário ao artigo atual
            comentario.save()
            return redirect('pagina_comentarios', artigo_id=artigo.id)
    else:
        form = ComentarioForm()

    return render(request, 'noticias/comentarios.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form
    })