# Generated by Django 3.2.8 on 2021-12-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_base64',
            field=models.TextField(blank=True, verbose_name='Сурет (Base64)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='youtube_link',
            field=models.TextField(blank=True, verbose_name='Видео (Ютуб)'),
        ),
    ]