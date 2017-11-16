from django.db import models
from django.conf import settings
from ticket.models import  Ticket
from paypal.standard.forms import PayPalPaymentsForm
from django.utils import timezone
# Create your models here.




class FeaturePay(models.Model):
    name = models.CharField(max_length=254)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payment')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
    #ticket = models.ForeignKey('ticket.Ticket')
    is_complete = models.BooleanField(default=False)

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "ticket_id": self.id,
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name
