from django.db import models
from django.conf import settings
from ticket.models import Ticket




class Vote(models.Model):
    ticket = models.ForeignKey(Ticket)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes')