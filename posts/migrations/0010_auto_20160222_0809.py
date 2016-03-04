# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20160221_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 22, 5, 9, 40, 189444, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
