# Generated by Django 4.2.2 on 2023-08-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chekigari', '0007_alter_shop_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
