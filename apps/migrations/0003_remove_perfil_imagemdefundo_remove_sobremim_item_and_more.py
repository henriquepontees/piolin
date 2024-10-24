# Generated by Django 5.0.5 on 2024-05-09 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_perfil_linklinkedin_perfil_linklinkedln_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='imagemdefundo',
        ),
        migrations.RemoveField(
            model_name='sobremim',
            name='item',
        ),
        migrations.RemoveField(
            model_name='sobremim',
            name='itemresposta',
        ),
        migrations.CreateModel(
            name='SobreMimItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=100, verbose_name='Item')),
                ('itemresposta', models.CharField(max_length=100, verbose_name='Resposta do item')),
                ('itens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.sobremim')),
            ],
        ),
    ]
