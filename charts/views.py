from django.shortcuts import render
#from Payment.models import FeaturePay
# Create your views here.
def charts(request):
    return render(request , 'charts/detail.html')