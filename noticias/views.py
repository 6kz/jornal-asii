from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario
from .forms import ComentarioForm

# ESTA É A FUNÇÃO QUE ESTÁ A FALTAR:
def home(request):
    artigos = Artigo.objects.all()
    return render(request, 'noticias/home.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'noticias/artigo.html', {'artigo': artigo})

def pagina_comentarios(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.save()
            return redirect('pagina_comentarios', artigo_id=artigo.id)
    else:
        form = ComentarioForm()

    return render(request, 'noticias/comentarios.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form
    })