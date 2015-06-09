# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        ('coffeemaker', '0004_auto_20150609_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cup',
            name='calendar_date_range',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(blank=True, null=True, verbose_name='Time range'),
        ),
    ]
