# Generated by Django 3.1.5 on 2021-01-28 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0024_auto_20210128_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]