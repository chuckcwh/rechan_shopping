# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0008_auto_20150404_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(default=b'ad_photos/default_img.png', null=True, upload_to=b'ad_photos', blank=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 11, 59, 58, 312512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 11, 59, 58, 309199, tzinfo=utc)),
        ),
    ]
