# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160220_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_rendered',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2016, 2, 21, 12, 55, 21, 984328, tzinfo=utc)),
        ),
    ]
