# Generated by Django 4.2.2 on 2023-06-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chekigari', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(max_length=6),
        ),
    ]
