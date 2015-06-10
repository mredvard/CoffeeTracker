# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffeemaker', '0007_auto_20150610_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255, blank=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('public', models.BooleanField(verbose_name='Public', default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('last_modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('created_by', models.ForeignKey(related_name='room_authors', verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('owls', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Owls')),
            ],
            options={
                'verbose_name': 'Coffee Room',
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddField(
            model_name='table',
            name='room',
            field=models.ForeignKey(to='coffeemaker.Room', null=True),
        ),
    ]
