from django.shortcuts import render

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
