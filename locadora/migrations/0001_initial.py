# Generated by Django 4.2.7 on 2023-11-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=255)),
                ('cartao', models.CharField(max_length=16)),
            ],
        ),
    ]
