# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-29 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_post', '0002_auto_20170629_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_owner',
            field=models.ManyToManyField(related_name='posts', to='student_post.Student'),
        ),
    ]
