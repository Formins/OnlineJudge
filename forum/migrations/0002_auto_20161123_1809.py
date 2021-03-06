# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-23 10:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.RemoveField(
            model_name='author',
            name='password',
        ),
        migrations.RemoveField(
            model_name='author',
            name='register_date',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
