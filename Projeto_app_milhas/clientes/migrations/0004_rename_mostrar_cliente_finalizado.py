# Generated by Django 4.1.7 on 2023-02-21 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_mostrar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Mostrar',
            new_name='Finalizado',
        ),
    ]