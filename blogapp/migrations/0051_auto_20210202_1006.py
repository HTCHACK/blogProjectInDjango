# Generated by Django 3.1.5 on 2021-02-02 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0050_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]