# Generated by Django 3.2.13 on 2022-06-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0011_auto_20220613_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='create_todo',
            field=models.DateField(verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='update_todo',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время последнего обновления'),
        ),
    ]
