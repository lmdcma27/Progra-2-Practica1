# Generated by Django 2.1.7 on 2019-04-12 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0008_archivos_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
