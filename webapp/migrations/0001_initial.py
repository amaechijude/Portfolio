# Generated by Django 5.0.4 on 2024-04-27 17:38

import django.core.validators
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=70, scale=None, size=[1920, 1080], upload_to='portfolio')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('messageTopic', models.CharField(max_length=100)),
                ('messageBody', models.TextField(max_length=1000)),
                ('createdAt_UTC', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('sub_title', models.CharField(blank=True, max_length=200)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=70, scale=None, size=[1920, 1080], upload_to='portfolio')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('github_url', models.URLField(blank=True, max_length=300, validators=[django.core.validators.URLValidator()])),
                ('link_url', models.URLField(blank=True, max_length=300, validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('job_desc', models.CharField(max_length=200)),
            ],
        ),
    ]
