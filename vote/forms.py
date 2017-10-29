
from django import forms
from .models import Vote

class CreateVoteForm(forms.ModelForm):
    ''' A form for creating a vote. '''

    class Meta:
            model = Vote
            exclude =  ['user']



