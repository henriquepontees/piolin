# Generated by Django 5.0.5 on 2024-05-09 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_experienciasprofissionaisitens_xp_resumoitens_resumo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experienciasprofissionaisitens',
            name='xp',
        ),
        migrations.RemoveField(
            model_name='resumoitens',
            name='resumo',
        ),
        migrations.AddField(
            model_name='experienciasprofissionais',
            name='xp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.experienciasprofissionaisitens'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumo',
            name='resumo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.resumoitens'),
            preserve_default=False,
        ),
    ]
