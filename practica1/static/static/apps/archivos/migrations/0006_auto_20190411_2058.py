# Generated by Django 2.1.7 on 2019-04-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0005_remove_archivos_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]