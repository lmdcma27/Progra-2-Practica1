# Generated by Django 2.1.7 on 2019-04-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0006_auto_20190411_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
