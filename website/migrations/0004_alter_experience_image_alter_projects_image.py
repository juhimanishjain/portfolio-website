# Generated by Django 4.0.5 on 2022-07-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_delete_aboutme_alter_experience_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
