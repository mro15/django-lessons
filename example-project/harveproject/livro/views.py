from django.shortcuts import render


# retorna o template que devolve "Ola mundo!"
def ola_mundo(request):
    # chamamos o template ola_mundo.html
    return render(request, 'ola_mundo.html')
