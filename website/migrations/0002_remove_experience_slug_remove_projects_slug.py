# Generated by Django 4.0.5 on 2022-07-10 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='slug',
        ),
    ]
