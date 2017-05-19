# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_chat_logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('text_sent', models.CharField(max_length=2000)),
                ('text_recieved', models.CharField(max_length=2000)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
