# Generated by Django 4.1.4 on 2022-12-11 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_fecha_creada_task_fecha_termino'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='fecha_termino',
            new_name='fecha_completada',
        ),
    ]