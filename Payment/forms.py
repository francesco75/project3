
from Payment import models
from Payment.models import FeaturePay
from django import forms


class CreateFeatureForm(forms.ModelForm):
    ''' A form for creating a new ticket. '''

    class Meta:
        model = FeaturePay
        exclude = ['user','is_complete','ticket']
