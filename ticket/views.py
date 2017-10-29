import datetime

from django.shortcuts import render, get_object_or_404


from ticket.forms import CreateTicketForm
from Payment.forms import CreateFeatureForm
from django.utils import timezone
from .models import Ticket
from django.shortcuts import redirect
from Payment.models import FeaturePay






"""
CRUD - create, retreive, update, delete
"""




def edit_ticket(request, id):
    post = get_object_or_404(Ticket, pk=id)
    if request.method == "POST":
        form = CreateTicketForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return render(request, ticket_detail, post.pk)
    else:
        form = CreateTicketForm(instance=post)
    return render(request, 'list/add_forms.html', {'form': form})


def tickets_list(request):
     '''Show a listed tickets'''
     form = Ticket.objects.all()
     return render(request,'list/listticket.html',{'form':form} )


def ticket_detail(request, id):
           ''' Show a particular ticket in the system. '''
           post = get_object_or_404(Ticket, pk=id)
           return render(request, "list/ticketdetail.html", {'post': post})


def create_ticket(request):
    ''' Add a new ticket to the system. '''
    if request.method == "POST":
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.save()
        return redirect(ticket_detail , list.pk )

    else:
        form = CreateTicketForm
    return render(request, 'list/add_forms.html', {
        'form': form
    })

def delete_ticket(request, id):
    ''''Delete the ticket to the system'''
    post = get_object_or_404(Ticket, pk=id)
    post.delete()
    return render(request,"list/delete_ticket.html")




##################  Vote ################


def vote_create(request):
    '''Show a listed votes'''
    form = Vote.objects.all()
    return render(request, 'votex/votelist.html', {'form': form})







