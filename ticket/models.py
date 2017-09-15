from django.utils import timezone
from django.db import models
import datetime

from django.conf import settings


TYPE_CHOICES = (
  ('bug', 'bug'),
  ('feature', 'feature'),
)


def _(param):
    pass


class Ticket(models.Model):
    '''
    Either a bug or feature ticket
    '''
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254,choices=TYPE_CHOICES, default=TYPE_CHOICES)
    content = models.TextField()
    date = models.DateField(_("Date"), default=datetime.date.today)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


