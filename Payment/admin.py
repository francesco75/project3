from django.contrib import admin
from .models import  FeaturePay

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'ticket')

admin.site.register(FeaturePay, PaymentAdmin)

# Register your models here.

