# Generated by Django 4.0.3 on 2022-03-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0002_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
