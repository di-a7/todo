# Generated by Django 5.1.4 on 2025-01-15 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='time_of_completion',
        ),
    ]
