# Generated by Django 5.0.5 on 2024-05-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_experienciasprofissionaisresumoitens_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacao', models.CharField(blank=True, max_length=150, verbose_name='Formação')),
                ('inicio', models.CharField(max_length=30, verbose_name='Ano de início do curso')),
                ('termino', models.CharField(max_length=30, verbose_name='Ano de término do curso')),
                ('instituicao', models.CharField(blank=True, max_length=150, verbose_name='Instituição')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciasProfissionais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Experiência')),
                ('inicio', models.CharField(max_length=30, verbose_name='Ano de início da experiência')),
                ('termino', models.CharField(max_length=30, verbose_name='Ano de término da experiência')),
                ('localidade', models.CharField(max_length=150, verbose_name='Local do Trabalho')),
            ],
        ),
        migrations.RenameModel(
            old_name='ExperienciasProfissionaisXpItem',
            new_name='ExperienciasProfissionaisItens',
        ),
        migrations.RenameModel(
            old_name='ExperienciasProfissionaisResumo',
            new_name='Resumo',
        ),
        migrations.RenameModel(
            old_name='ExperienciasProfissionaisResumoItens',
            new_name='ResumoItens',
        ),
        migrations.DeleteModel(
            name='ExperienciasProfissionaisEducacao',
        ),
        migrations.DeleteModel(
            name='ExperienciasProfissionaisXp',
        ),
        migrations.RenameField(
            model_name='resumo',
            old_name='descricaoresumo',
            new_name='descricao',
        ),
    ]
