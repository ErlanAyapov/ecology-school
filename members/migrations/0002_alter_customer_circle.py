# Generated by Django 3.2.3 on 2021-05-25 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='circle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circle.group'),
        ),
    ]
