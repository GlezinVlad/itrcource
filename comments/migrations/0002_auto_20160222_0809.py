# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_published',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 22, 5, 9, 40, 191579, tzinfo=utc)),
        ),
    ]
