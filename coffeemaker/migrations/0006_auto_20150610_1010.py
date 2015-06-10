# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffeemaker', '0005_auto_20150609_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='room',
            name='owls',
        ),
        migrations.RemoveField(
            model_name='table',
            name='room',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
