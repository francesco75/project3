
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse
from ticket.models import Ticket
from Payment.forms import CreateFeatureForm
from Payment.models import FeaturePay



# Create your views here.


############# Create  Payment#########
def pay_form(request):
         if request.method == "POST":
            form = CreateFeatureForm(request.POST)
            if form.is_valid():
                FeaturePay = form.save(commit=False)
                FeaturePay.user = request.user
                FeaturePay.save()


            return render(request, "features/featuredetail.html", {'FeaturePay': FeaturePay})


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




def payment_finish(request):


    return render(request, 'features/paypal-complete.html')





def payment_complete(request,id):
    '''
    When paypal payment is complete, we returned to this view
    to finialise the payment model instance, marking it as "is_complete=True"
    '''
    payment = FeaturePay.objects.get(id)
    payment.is_complete = True
    payment.save()
    return render(request, 'features/paypal-return.html')



############# List Payments ########################


def  list_feature(request):
    '''Show a listed Feature'''
    form = FeaturePay.objects.all()
    return render( request, 'features/featurelist.html', {'form': form})



def payment_stats(request):
    payments = FeaturePay.objects.all()
    data = []
    for payment in payments:
        data.append({
            'price': payment.price,
            'feature_name': payment.ticket.name,
            'date': payment.date
        })
    return JsonResponse(data)













