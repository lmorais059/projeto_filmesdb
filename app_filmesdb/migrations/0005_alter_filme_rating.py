# Generated by Django 3.2.25 on 2024-04-25 02:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_filmesdb', '0004_auto_20240424_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
