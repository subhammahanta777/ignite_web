# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0005_auto_20170509_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_bank',
            name='visited',
            field=models.BooleanField(default=False),
        ),
    ]