# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_published',
            field=models.DateField(default=datetime.date(2016, 2, 20)),
        ),
        migrations.AddField(
            model_name='post',
            name='template_name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
