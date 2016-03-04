# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160220_0620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='about',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2016, 2, 20, 14, 59, 1, 321744, tzinfo=utc)),
        ),
    ]
