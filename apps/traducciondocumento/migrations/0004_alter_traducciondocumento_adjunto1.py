# Generated by Django 3.2.6 on 2023-01-03 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traducciondocumento', '0003_alter_traducciondocumento_adjunto1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traducciondocumento',
            name='adjunto1',
            field=models.FileField(upload_to='upload/', verbose_name='Adjuntar'),
        ),
    ]