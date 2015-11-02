# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0014_auto_20150520_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='title',
            new_name='name',
        ),
    ]
