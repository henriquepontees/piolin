# Generated by Django 5.0.5 on 2024-05-09 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_rename_item_resumoitem_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumoitem',
            old_name='descricao',
            new_name='item',
        ),
    ]
