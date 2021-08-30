from django.urls import path

from . import views

app_name = 'livro'
urlpatterns = [
    path('', views.ola_mundo, name='ola_mundo'),
    path('livros/', views.exibe_livros, name='exibe_livros'),
    path('livros/<int:indice_livro>/', views.detalhe_livro, name='detalhe_livro'),
    path('livros/cadastro', views.novo_livro, name='cadastro_livro')
]
