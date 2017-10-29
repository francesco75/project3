from django.db import models
from django.conf import settings
from ticket.models import  Ticket
from paypal.standard.forms import PayPalPaymentsForm
# Create your models here.




class FeaturePay(models.Model):
    name = models.CharField(max_length=254)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payment')
    price = models.DecimalField(max_digits=6, decimal_places=2)





    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "ticket_id": self.id,
            "notify_url": settings.PAYPAL_NOTIFY_URL,

        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name
