# Generated by Django 4.1.4 on 2022-12-11 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='fecha_termino',
            new_name='fecha_creada',
        ),
    ]