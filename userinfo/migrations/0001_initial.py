# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('date_of_birth', models.DateField(blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('info', models.TextField(blank=True)),
                ('interests', models.TextField(blank=True)),
                ('language', models.CharField(max_length=10, default='English')),
                ('theme', models.CharField(max_length=10, default='light')),
            ],
        ),
    ]
