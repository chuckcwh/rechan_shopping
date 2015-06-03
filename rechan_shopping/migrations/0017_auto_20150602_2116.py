# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0016_auto_20150525_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(default=b'ad_photos/default_img.jpg', upload_to=b'ad_photos', blank=True, help_text=b'use 2833px width x 1375px height jpg or photos in similar aspect ratio', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=b'product_photos/default_img.jpg', upload_to=b'product_photos', blank=True, help_text=b'use 480x480px jpg or bigger square photo', null=True),
        ),
    ]
