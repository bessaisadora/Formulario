from django.contrib import admin
from django.urls import path
from main.views import cadastro_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastroaluno/', cadastro_aluno, name='cadastro_aluno')
]