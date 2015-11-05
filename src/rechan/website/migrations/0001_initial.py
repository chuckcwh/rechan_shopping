# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('real_name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('activated', models.BooleanField(default=True)),
                ('image', models.ImageField(default=b'ad_photos/default_img.jpg', upload_to=b'ad_photos', blank=True, help_text=b'use 2833px width x 1375px height jpg or photos in similar aspect ratio', null=True)),
                ('publish_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bosstalk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=15, choices=[(b'Murmur', b'Murmur'), (b'Toptalk', b'Toptalk'), (b'Smalltip', b'Smalltip')])),
                ('title', models.CharField(help_text=b'only Toptalks have titles!', max_length=150, null=True, blank=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buy_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(related_name='buylist_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipient', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(related_name='contact_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=20, choices=[(b'Toys', b'Toys'), (b'Candies', b'Candies'), (b'Lucky_draw', b'Lucky_draw')])),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100, null=True, blank=True)),
                ('have', models.BooleanField(default=True)),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('discount_S', models.BooleanField(default=False)),
                ('discount_price', models.PositiveSmallIntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
                ('photo', models.ImageField(default=b'product_photos/default_img.jpg', upload_to=b'product_photos', blank=True, help_text=b'use 480x480px jpg or bigger square photo', null=True)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('buyer', models.ManyToManyField(related_name='prod_buyers', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='prod_tags', to='website.Tag', blank=True),
        ),
    ]
