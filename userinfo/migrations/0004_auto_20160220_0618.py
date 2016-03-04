# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_userinfo_avatar_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar_url',
            field=models.URLField(blank=True, default='http://res.cloudinary.com/dusvendql/image/upload/v1455886667/blrym6ryw2w3n9m6qveg.png'),
        ),
    ]
