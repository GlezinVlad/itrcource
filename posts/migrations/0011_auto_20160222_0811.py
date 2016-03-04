# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20160222_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 22, 5, 11, 2, 303909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='media_url',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
