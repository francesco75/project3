import uuid
from django import template
from Payment.models import FeaturePay
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

register = template.Library()


def paypal_form_for(FeaturePay, user):
    if user.is_subscribed(FeaturePay):
        html = "Subscribed!"
    else:
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "currency_code": "USD",
            "cmd": "_xclick-subscriptions",
            "a3": FeaturePay.price,
            "p3": 1,
            "t3": "M",
            "src": 1,
            "sra": 1,
            "FeaturePay_name": FeaturePay.name,
            "invoice": uuid.uuid4(),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "paypal_cancel": "%s/paypal_cancel/" % settings.SITE_URL,
            "custom": "%s-%s" % (FeaturePay.id, user.id)

        }
        if settings.DEBUG:
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').sandbox()
        else:
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').render()

    return html


register.simple_tag(paypal_form_for)