# Generated by Django 2.1.7 on 2019-04-11 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0004_archivos_propietario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivos',
            name='name',
        ),
    ]
