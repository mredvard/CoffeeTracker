# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('coffeemaker', '0002_auto_20150609_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cup',
            name='repeat_days',
            field=django.contrib.postgres.fields.ArrayField(verbose_name='Days to be repeated', base_field=models.PositiveSmallIntegerField(choices=[(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')]), null=True, size=12, blank=True),
        ),
        migrations.AlterField(
            model_name='cup',
            name='repeat_months',
            field=django.contrib.postgres.fields.ArrayField(verbose_name='Months to be repeated', base_field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]), null=True, size=12, blank=True),
        ),
    ]
