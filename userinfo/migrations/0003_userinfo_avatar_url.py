# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20160214_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='avatar_url',
            field=models.URLField(blank=True),
        ),
    ]
