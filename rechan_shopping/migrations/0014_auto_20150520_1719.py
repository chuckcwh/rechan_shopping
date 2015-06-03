# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0013_auto_20150417_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(related_name='buylist_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='discount_S',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ads',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
