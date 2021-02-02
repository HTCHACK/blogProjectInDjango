# Generated by Django 3.1.5 on 2021-01-27 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_remove_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('author', models.CharField(max_length=20)),
                ('topic', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
