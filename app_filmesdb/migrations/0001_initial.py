# Generated by Django 3.2.25 on 2024-04-20 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id_filme', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('diretor', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
