# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160220_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2016, 2, 20, 3, 20, 22, 49840, tzinfo=utc)),
        ),
    ]
