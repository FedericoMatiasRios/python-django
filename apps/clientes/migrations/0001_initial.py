# Generated by Django 4.1.7 on 2023-03-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('apellido', models.CharField(max_length=254)),
                ('dni', models.CharField(blank=True, max_length=12, null=True, verbose_name='D.N.I.')),
            ],
        ),
    ]
