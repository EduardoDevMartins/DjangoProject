# Generated by Django 4.1.7 on 2023-02-21 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Categoria',
            new_name='Compania',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Cia',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Sobrenome',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Origem',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.origem'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Login',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Milheiro',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Senha',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
