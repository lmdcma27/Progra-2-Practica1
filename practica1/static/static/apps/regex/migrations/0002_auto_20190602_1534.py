# Generated by Django 2.1.7 on 2019-06-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regex', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regex',
            name='id',
        ),
        migrations.AlterField(
            model_name='regex',
            name='regex',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]
