# Generated by Django 4.1.4 on 2022-12-11 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_fecha_termino_task_fecha_completada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='fecha_completada',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]