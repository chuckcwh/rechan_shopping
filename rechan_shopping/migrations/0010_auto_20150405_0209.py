# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0009_auto_20150404_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 18, 9, 24, 688779, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=b'product_photos/default_img.png', null=True, upload_to=b'product_photos', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 18, 9, 24, 685996, tzinfo=utc)),
        ),
    ]
