# Generated by Django 3.2.6 on 2023-01-02 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistenciaespecializada', '0004_alter_asistenciaespecializada_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistenciaespecializada',
            name='tipo',
            field=models.CharField(choices=[('Tesis', 'Tesis'), ('Posgrado', 'Posgrado'), ('Curso', 'Curso')], default='1', max_length=40, verbose_name='Tipo'),
        ),
    ]
