# Generated by Django 3.1.5 on 2021-01-28 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_auto_20210128_0521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='blogpost_connected',
            new_name='com',
        ),
    ]