from django.db import models
#No topo criamos as listas referentes aos atributos utilizados na classe alunos
LISTA_SEXO= [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]

LISTA_CURSO= [
    ('ADS', 'ADS'),
    ('Agronomia', 'Agronomia'),
    ('Química', 'Química'),
]
#Criamos o modelo para cadastro de minicursos
class Minicurso(models.Model):
    nome_minicurso = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome_minicurso

#Criamos o modelo para cadastro de alunos
class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, default='SOME STRING')
    data_nascimento = models.DateTimeField()
    email = models.EmailField()
    endereço = models.CharField(max_length=150)
    sexo = models.CharField(max_length=150, choices=LISTA_SEXO)
    curso = models.CharField(max_length=150, choices=LISTA_CURSO)
    minicursos = models.ManyToManyField(Minicurso)

    def __str__(self) -> str:
        return self.nome
