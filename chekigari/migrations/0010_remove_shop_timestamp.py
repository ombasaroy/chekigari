# Generated by Django 4.2.2 on 2023-08-05 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chekigari', '0009_remove_shop_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='timeStamp',
        ),
    ]