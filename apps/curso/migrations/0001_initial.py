# Generated by Django 3.2.6 on 2022-11-29 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre del curso')),
                ('ano', models.IntegerField(max_length=4, verbose_name='Año')),
                ('tema', models.TextField(verbose_name='Tema del curso')),
            ],
        ),
    ]
