# Generated by Django 4.2.2 on 2023-06-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('onames', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('dob', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
