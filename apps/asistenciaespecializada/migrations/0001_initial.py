# Generated by Django 3.2.6 on 2023-01-02 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsistenciaEspecializada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'Tesis'), ('2', 'Posgrado'), ('3', 'Curso')], default='1', max_length=40, verbose_name='Tipo')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('respuesta', models.TextField(null=True, verbose_name='Respuesta')),
            ],
        ),
    ]
