# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffeemaker', '0006_auto_20150610_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='table',
            name='owl',
        ),
        migrations.AddField(
            model_name='table',
            name='owls',
            field=models.ManyToManyField(verbose_name='Owls', to=settings.AUTH_USER_MODEL),
        ),
    ]
