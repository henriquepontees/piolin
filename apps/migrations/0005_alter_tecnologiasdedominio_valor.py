# Generated by Django 5.0.5 on 2024-05-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_remove_sobremimitem_itens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnologiasdedominio',
            name='valor',
            field=models.IntegerField(verbose_name='Valor'),
        ),
    ]
