# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0017_auto_20150602_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bosstalk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=15, choices=[(b'Murmur', b'Murmur'), (b'Toptalk', b'Toptalk'), (b'Smalltip', b'Smalltip')])),
                ('title', models.CharField(help_text=b'only Toptalks have titles!', max_length=150, null=True, blank=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
