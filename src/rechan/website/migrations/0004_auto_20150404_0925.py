# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0003_auto_20150404_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(default=b'../rechan_shopping/static/img/default_img.png', null=True, upload_to=b'ad_photos', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=b'../rechan_shopping/static/img/default_img.png', null=True, upload_to=b'product_photos', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 9, 25, 32, 660160, tzinfo=utc)),
        ),
    ]
