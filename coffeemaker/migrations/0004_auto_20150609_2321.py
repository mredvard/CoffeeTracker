# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        ('coffeemaker', '0003_auto_20150609_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cup',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='Due date', blank=True),
        ),
        migrations.AlterField(
            model_name='cup',
            name='repeat_date_range',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(null=True, verbose_name='Repeat date range', blank=True),
        ),
    ]
