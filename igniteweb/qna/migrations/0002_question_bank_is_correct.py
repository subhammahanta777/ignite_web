# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_bank',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]