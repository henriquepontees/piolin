# Generated by Django 5.0.5 on 2024-05-10 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_rename_descricao_resumoitem_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experienciasprofissionaisitem',
            old_name='resumo',
            new_name='xp',
        ),
        migrations.AlterField(
            model_name='experienciasprofissionaisitem',
            name='item',
            field=models.CharField(max_length=150, verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='resumoitem',
            name='item',
            field=models.CharField(max_length=150, verbose_name='Item'),
        ),
        migrations.CreateModel(
            name='FotosDoProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('imagem', models.ImageField(upload_to='projetos', verbose_name='Foto')),
                ('projetos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='apps.projetos')),
            ],
        ),
    ]
