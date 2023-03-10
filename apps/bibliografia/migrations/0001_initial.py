# Generated by Django 3.2.6 on 2022-12-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40, verbose_name='Título')),
                ('autor', models.CharField(max_length=40, verbose_name='Autor')),
                ('anno', models.PositiveSmallIntegerField(max_length=4, verbose_name='Año')),
                ('editorial', models.CharField(max_length=25, verbose_name='Editorial')),
                ('ciudad', models.CharField(max_length=25, verbose_name='Ciudad')),
            ],
        ),
    ]
