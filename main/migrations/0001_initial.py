# Generated by Django 4.1.4 on 2022-12-10 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minicurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(default='SOME STRING', max_length=14)),
                ('data_nascimento', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('endereço', models.CharField(max_length=150)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=150)),
                ('curso', models.CharField(choices=[('ADS', 'ADS'), ('Agronomia', 'Agronomia'), ('Química', 'Química')], max_length=150)),
                ('minicursos', models.ManyToManyField(to='main.minicurso')),
            ],
        ),
    ]
