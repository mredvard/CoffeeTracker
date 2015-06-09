from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .rooms import Room


class Table(models.Model):

    class Meta:
        verbose_name = _('Coffee Table')
        app_label = "coffeemaker"
        ordering = ['-date_created']

    created_by = models.ForeignKey(User, verbose_name=_('Author'), related_name='table_authors')
    owl = models.ForeignKey(User, verbose_name=_('Owl'), related_name='table_owls')
    room = models.ForeignKey(Room, verbose_name=_('Room'))
    followers = models.ManyToManyField(User, verbose_name=_('Followers'))
    title = models.CharField(_('Title'), max_length=255, blank=True)
    description = models.TextField(_('Description'), blank=True)
    public = models.BooleanField(_('Public'), default=False)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True)
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.title
