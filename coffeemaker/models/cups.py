from django.contrib.auth.models import User
from django.contrib.postgres import fields as pg_fields
from django.db import models
from django.utils.dates import WEEKDAYS_ABBR, MONTHS
from django.utils.translation import ugettext_lazy as _

from .tables import Table


class Cup(models.Model):

    INTERVAL_CHOICES = ((0, _('Daily')), (1, _('Weekly')), (2, _('Monthly')))

    class Meta:
        verbose_name = _('Coffee Cup')
        app_label = "coffeemaker"
        ordering = ['-date_created']

    created_by = models.ForeignKey(User, verbose_name=_('Author'), related_name='cup_authors')
    owl = models.ForeignKey(User, verbose_name=_('Owl'), related_name='cup_owls')
    table = models.ForeignKey(Table, verbose_name=_('Table'))
    followers = models.ManyToManyField(User)
    title = models.CharField(_('Title'), max_length=255, blank=True)
    description = models.TextField(_('Description'), blank=True)
    completed = models.BooleanField(_('Completed'), default=False)
    public = models.BooleanField(_('Public'), default=False)
    locked = models.BooleanField(_('Locked'), default=False)

    # Repetitive tasks
    set_to_repeat = models.BooleanField(_('Set to repeat'), default=False)
    repeat_interval = models.PositiveSmallIntegerField(
        verbose_name=_('Repeat interval'), choices=INTERVAL_CHOICES, blank=True)
    repeat_months = pg_fields.ArrayField(
        verbose_name=_('Months to be repeated'),
        base_field=models.PositiveSmallIntegerField(choices=MONTHS.items()),
        size=12,
        blank=True
    )
    repeat_days = pg_fields.ArrayField(
        verbose_name=_('Days to be repeated'),
        base_field=models.PositiveSmallIntegerField(
            choices=WEEKDAYS_ABBR.items()),
        size=12,
        blank=True,
    )
    repeat_date_range = pg_fields.DateTimeRangeField(
        verbose_name=_('Repeat date range'), blank=True)

    # Time information
    calendar_date_range = pg_fields.DateTimeRangeField(
        _('Time range'), blank=True)
    due_date = models.DateTimeField(_('Due date'), blank=True)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True)
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.title
