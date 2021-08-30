from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Livro


# retorna o template que devolve "Ola mundo!"
def ola_mundo(request):
    # chamamos o template ola_mundo.html
    return render(request, 'ola_mundo.html')


# view responsavel por carregar todos os livros e repassar para o template
def exibe_livros(request):
    livros = Livro.objects.all()
    context = {'lista_livros': livros}
    return render(request, 'exibe_livros.html', context=context)


# view responsavel por carregar um livro dado o indice
def detalhe_livro(request, indice_livro):
    livro = get_object_or_404(Livro, pk=indice_livro)
    context = {'livro': livro}
    return render(request, 'detalhe_livro.html', context)
