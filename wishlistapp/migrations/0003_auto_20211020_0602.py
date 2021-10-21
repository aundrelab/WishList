# Generated by Django 3.2.7 on 2021-10-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlistapp', '0002_auto_20210929_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imageURL',
            field=models.URLField(max_length=500, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemURL',
            field=models.URLField(max_length=500, verbose_name='Item URL'),
        ),
    ]
