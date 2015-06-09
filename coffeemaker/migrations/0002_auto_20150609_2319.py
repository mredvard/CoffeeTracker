# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
from django.conf import settings
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffeemaker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('date_created', models.DateTimeField(verbose_name='Date Created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('created_by', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL, related_name='log_authors')),
            ],
            options={
                'verbose_name': 'Coffee Log',
                'ordering': ['-date_created'],
            },
        ),
        migrations.AlterModelOptions(
            name='cup',
            options={'verbose_name': 'Coffee Cup', 'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Coffee Room', 'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'Coffee Table', 'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='cup',
            name='followers',
            field=models.ManyToManyField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cup',
            name='owl',
            field=models.ForeignKey(verbose_name='Owl', null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='cup_owls'),
        ),
        migrations.AlterField(
            model_name='cup',
            name='repeat_date_range',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(verbose_name='Repeat date range', blank=True),
        ),
        migrations.AlterField(
            model_name='cup',
            name='repeat_days',
            field=django.contrib.postgres.fields.ArrayField(verbose_name='Days to be repeated', size=12, blank=True, base_field=models.PositiveSmallIntegerField(choices=[(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')])),
        ),
        migrations.AlterField(
            model_name='cup',
            name='repeat_interval',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Daily'), (1, 'Weekly'), (2, 'Monthly')], verbose_name='Repeat interval', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cup',
            name='repeat_months',
            field=django.contrib.postgres.fields.ArrayField(verbose_name='Months to be repeated', size=12, blank=True, base_field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
        ),
        migrations.AlterField(
            model_name='cup',
            name='table',
            field=models.ForeignKey(verbose_name='Table', null=True, to='coffeemaker.Table', blank=True),
        ),
        migrations.AddField(
            model_name='log',
            name='cup',
            field=models.ForeignKey(verbose_name='Cup', null=True, to='coffeemaker.Cup', blank=True),
        ),
    ]
