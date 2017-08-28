from django.shortcuts import render, get_object_or_404
from ticket.forms import CreateTicketForm
from django.utils import timezone
from .models import Ticket
from django.shortcuts import redirect


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
    return render(request, 'add_forms.html', {'form': form})


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
            list.date  = timezone.now()
            list.save()
        return redirect(ticket_detail , list.pk )

    else:
        form = CreateTicketForm()
    return render(request, 'add_forms.html', {
        'form': form
    })

def delete_ticket(request, id):
    ''''Delete the ticket to the system'''
    post = get_object_or_404(Ticket, pk=id)
    post.delete()
    return render(request,"delete_ticket.html")
    #return redirect(ticket_detail,post.id)











# class CreateTicketView(generic.detail.DetailView):
#     ''' Create a new ticket.'''
#     form_class = CreateTicketForm
#
#
#     # def post(self):
#     #
#     #   #if self.form_class.data['type'] == 'feature':
#     #    #   return render(request, "add_forms.html", {"form_class": form_class})
#     #   #if self.form_data['type'] == 'bug':
#     #    #   return render(request, "add_forms.html", {"form_class": form_class})
#     #
#     #        if self.form_data['type'] == 'feature':
#     #            def server_create(request, template_name='add_forms.html'):
#     #                form = ServerForm(request.POST or None)
#     #                if form.is_valid():
#     #                    form.save()
#     #                    return redirect('server_list')
#     #                return render(request, template_name, {'form_class': form_class})
#     #
#     #            #return render(request, "add_forms.html", {"form_class": form_class})
#     #            ###Create the feature with paypal
#     #
#     #        if self.form_data['type'] == 'bug':
#     #            return render(request, "add_forms.html", {"form_class": form_class})
#
