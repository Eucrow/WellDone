# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
        ('comentary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentary',
            name='author',
        ),
        migrations.AddField(
            model_name='comentary',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='comentary',
            name='post',
        ),
        migrations.AddField(
            model_name='comentary',
            name='post',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
            preserve_default=False,
        ),
    ]