# Generated by Django 2.1.7 on 2019-03-25 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('carnet', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('correo', models.EmailField(max_length=30)),
                ('cui', models.CharField(max_length=30)),
                ('profesion', models.CharField(choices=[('00', 'Licenciatura en Matemática'), ('01', 'Licenciatura en Física')], max_length=2)),
            ],
        ),
    ]
