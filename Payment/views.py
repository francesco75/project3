
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from ticket.models import Ticket
from Payment.forms import CreateFeatureForm
from Payment.models import FeaturePay




# Create your views here.

def pay_form(request):
############# Create  Payment#########

         if request.method == "POST":
            form = CreateFeatureForm(request.POST)
            if form.is_valid():
                FeaturePay = form.save(commit=False)
                FeaturePay.user = request.user
                FeaturePay.save()


            return render(request, 'votex/votedetail.html')

         else :

            form =  CreateFeatureForm

         return render(request , 'features/payfeature.html',  {
           'form': form

        })







def payment_form(request, id):
############# Create  Payment#########
         ticket = get_object_or_404(Ticket, id=id)


         if request.method == "POST":
            form = CreateFeatureForm(request.POST,request.FILES, instance=ticket)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.user = request.user
                ticket.save()


            return redirect( 'ticket_detail',id)
         else :

              form = CreateFeatureForm(instance=ticket)
         return render(request , 'features/payfeature.html',  {
           'form': form,

        })


############# List Payments ########################


def  list_feature(request):
    '''Show a listed Feature'''
    form = FeaturePay.objects.all()
    return render( request, 'features/featurelist.html', {'form': form})



















# def payment_form(request,id):
# ############# Create  Payment#########
#          ticket = get_object_or_404(Ticket, id=id)
#          if request.method == "POST":
#             form = CreateFeatureForm(request.POST,instance=ticket)
#             if form.is_valid():
#                 FeaturePay = form.save(commit=False)
#                 FeaturePay.user = request.user
#                 FeaturePay.save()
#
#                 #tickets = Ticket.objects.filter(type='Payment')
#                  #for ticket in tickets:
#                 #     pass
#
#             return render(request, 'votex/votedetail.html')
#          else :
#
#             form =  CreateFeatureForm(instance='ticket')
#
#          return render(request , 'features/payfeature.html',  {
#            'form': form
#
#         })
