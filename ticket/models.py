from django.utils import timezone
from django.db import models
import datetime

from django.conf import settings


TYPE_CHOICES = (
  ('bug', 'bug'),
  ('feature', 'feature'),
)
STAT = (
    ('To Do','To Do'),
    ('Doing', 'Doing'),
    ('Done', 'Done'),
)

def _(param):
    pass


class Ticket(models.Model):
    '''
    Either a bug or Payment ticket
    '''
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254,choices=TYPE_CHOICES, default=TYPE_CHOICES)
    content = models.TextField()
    date = models.DateField(_("Date"), default=datetime.date.today)
    status = models.CharField(max_length=254, choices=STAT, default=STAT)
    resolved = models.BooleanField(default=False)


    def __str__(self):
        return self.name


