# Generated by Django 4.1 on 2022-09-13 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascotas',
            old_name='nombre',
            new_name='animal',
        ),
        migrations.RemoveField(
            model_name='mascotas',
            name='raza',
        ),
    ]