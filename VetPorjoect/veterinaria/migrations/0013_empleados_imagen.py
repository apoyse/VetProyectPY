# Generated by Django 4.0.3 on 2022-05-02 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0012_delete_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='imagen',
            field=models.ImageField(null=True, upload_to='empleados/'),
        ),
    ]
