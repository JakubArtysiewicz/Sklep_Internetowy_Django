# Generated by Django 4.2.7 on 2024-10-30 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkt',
            name='nazwa',
        ),
    ]
