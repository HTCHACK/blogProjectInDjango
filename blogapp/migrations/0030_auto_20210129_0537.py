# Generated by Django 3.1.5 on 2021-01-29 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0029_auto_20210129_0527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'entries'},
        ),
    ]