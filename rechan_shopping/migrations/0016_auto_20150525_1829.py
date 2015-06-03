# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0015_auto_20150523_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(default=b'ad_photos/default_img.jpg', null=True, upload_to=b'ad_photos', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=b'product_photos/default_img.jpg', null=True, upload_to=b'product_photos', blank=True),
        ),
    ]
