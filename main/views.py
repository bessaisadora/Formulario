# Transformamos o arquivo forms em um html
from django.shortcuts import render
from main.forms import AlunoForm


def cadastro_aluno(request):
    if request.method == 'POST': #Se eu quero cadastrar (POST)
        forms = AlunoForm(request.POST) #Preenche as informações
        if forms.is_valid(): #Verifica se há algum erro de preenchimento (falta algo, por ex)
            forms.save() #Se não houver erro, salva o forms
            forms = AlunoForm() #Zera as informações preenchidas

    else: #Se eu quero carregar as informações, basta carregar o forms
        forms = AlunoForm()
        
    return render(request,'form.html', { 'form' : forms})
