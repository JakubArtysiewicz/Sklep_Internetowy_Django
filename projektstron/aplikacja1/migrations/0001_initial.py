# Generated by Django 4.2.7 on 2024-10-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.CharField(max_length=100)),
            ],
        ),
    ]
