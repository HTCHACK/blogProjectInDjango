# Generated by Django 3.1.5 on 2021-01-27 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_remove_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
