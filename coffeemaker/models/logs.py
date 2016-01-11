from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .cups import Cup


class Log(models.Model):

    class Meta:
        verbose_name = _('Coffee Log')
        app_label = "coffeemaker"
        ordering = ['-date_created']

    created_by = models.ForeignKey(
        User, verbose_name=_('Author'), related_name='log_authors')
    cup = models.ForeignKey(Cup, blank=True, null=True, verbose_name=_('Cup'))
    description = models.TextField(_('Description'), blank=True)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True)
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.description
