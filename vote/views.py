import datetime
from django.shortcuts import render, get_object_or_404
from .models import Ticket
from django.shortcuts import redirect
from vote.models import Vote
from Payment.forms import CreateFeatureForm
from Payment.models import FeaturePay
from django.contrib import messages






def create_vote(request, id):
    ''' Add a new vote to the system. '''

    # TODO:
    # - only allow a user to vote once on each ticket
    # - include the time that the vote was registered
    # - display a confirmation message in the template using the django messaging system

    ticket = get_object_or_404(Ticket, id=id)
    vote = Vote(ticket=ticket, user=request.user)


    if ticket.type == 'Payment':
        vote.completed = True
        vote.save()
        #  Confirm Success message ######
        messages.success(request,
                         "Your Vote has been added to the Payment Feature!")

        return redirect('payment_form',id)



    else:
        # is a bug
        vote.completed = True
        vote.save()

        # Add confirmation message
        messages.success(request,
                         "Your Vote has been added to the bug!")

    return redirect('ticket_detail', id)
