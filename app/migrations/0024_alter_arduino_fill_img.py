# Generated by Django 4.1.4 on 2023-01-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_arduino_fill_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arduino',
            name='fill_img',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='fill_img'),
        ),
    ]
