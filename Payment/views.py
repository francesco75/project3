from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse
from ticket.models import Ticket
from Payment.forms import CreateFeatureForm
from Payment.models import FeaturePay
from vote.models import Vote

def payment_form(request, id):
############# Create  Payment#########
         ticket = get_object_or_404(Ticket, id=id)
         if request.method == "POST":
            print('test')
            form = CreateFeatureForm(request.POST)
            if form.is_valid():
                payment = form.save(commit=False)
                payment.ticket = ticket
                payment.user = request.user
                payment.is_complete = True
                payment.save()
                return redirect('payment_detail', payment.id)
         else :
              form = CreateFeatureForm()
         return render(request , 'features/payfeature.html',  {
           'form': form,
            'ticket': ticket
        })


def payment_detail(request, id):
    payment = get_object_or_404(FeaturePay, pk=id)
    return render(request, "payments/payment_detail.html", {'payment': payment})


def payment_finish(request):
    return render(request, 'features/paypal-complete.html')

def paypal_cancel(request,id):
    post = get_object_or_404(FeaturePay, pk=id)
    form = Vote.objects.last()
    form.delete()
    post.delete()
    return render(request, 'features/paypal_cancel.html')




# def payment_complete(request,id):
#     '''
#     When paypal payment is complete, we returned to this view
#     to finialise the payment model instance, marking it as "is_complete=True"
#     '''
#     payment = FeaturePay.objects.get(id)
#     payment.is_complete = True
#     payment.save()
#     return render(request, 'features/paypal-return.html')



############# List Payments ########################














