# Generated by Django 3.1.5 on 2021-01-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0038_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=130),
        ),
    ]
