# Generated by Django 3.2.13 on 2022-06-09 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20220609_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authortodo',
            name='last_note',
        ),
    ]