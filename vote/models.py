from django.db import models
from django.conf import settings
from ticket.models import Ticket

# Vote.objects.filter(ticket=...., completed=True)


class Vote(models.Model):
    ticket = models.ForeignKey(Ticket)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes')
    completed = models.BooleanField(default=False)

