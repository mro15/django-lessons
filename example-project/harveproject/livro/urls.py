from django.urls import path

from . import views

app_name = 'livro'
urlpatterns = [
    path('', views.ola_mundo, name='ola_mundo'),
    path('livros/', views.exibe_livros, name='exibe_livros')
]
