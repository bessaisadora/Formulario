# Generated by Django 4.1.4 on 2022-12-10 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_aluno_minicursos_delete_minicurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minicurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_minicurso', models.CharField(max_length=150)),
            ],
        ),
    ]