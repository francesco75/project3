
from django import forms
from .models import Ticket
from ticket import models


class CreateTicketForm(forms.ModelForm):
    ''' A form for creating a new ticket. '''

    class Meta:
        model = models.Ticket
        fields = "__all__"




