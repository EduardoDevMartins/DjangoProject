# Generated by Django 4.1.7 on 2023-02-21 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_alter_cliente_finalizado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Finalizado',
            new_name='Ativo',
        ),
    ]
