# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 9, 9, 7, 159667, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
