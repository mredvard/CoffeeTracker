# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, blank=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('locked', models.BooleanField(default=False, verbose_name='Locked')),
                ('set_to_repeat', models.BooleanField(default=False, verbose_name='Set to repeat')),
                ('repeat_interval', models.PositiveSmallIntegerField(choices=[(0, 'Daily'), (1, 'Weekly'), (2, 'Monthly')], verbose_name='Repeat interval')),
                ('repeat_months', django.contrib.postgres.fields.ArrayField(size=12, base_field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]), verbose_name='Months to be repeated')),
                ('repeat_days', django.contrib.postgres.fields.ArrayField(size=12, base_field=models.PositiveSmallIntegerField(choices=[(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')]), verbose_name='Days to be repeated')),
                ('repeat_date_range', django.contrib.postgres.fields.ranges.DateTimeRangeField(blank=True, verbose_name='Start and end of the repeptitive cycle')),
                ('calendar_date_range', django.contrib.postgres.fields.ranges.DateTimeRangeField(blank=True, verbose_name='Time range')),
                ('due_date', models.DateTimeField(blank=True, verbose_name='Due date')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('last_modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='cup_authors', verbose_name='Author')),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('owl', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='cup_owls', verbose_name='Owl')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Coffee Cups',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, blank=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('last_modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='room_authors', verbose_name='Author')),
                ('owls', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='room_owls', verbose_name='Owls')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Coffee Rooms',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, blank=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('last_modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='table_authors', verbose_name='Author')),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Followers')),
                ('owl', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='table_owls', verbose_name='Owl')),
                ('room', models.ForeignKey(to='coffeemaker.Room', verbose_name='Room')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Coffee Tables',
            },
        ),
        migrations.AddField(
            model_name='cup',
            name='table',
            field=models.ForeignKey(to='coffeemaker.Table', verbose_name='Table'),
        ),
    ]
