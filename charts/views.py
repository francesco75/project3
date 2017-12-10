from django.shortcuts import render
from django.http import JsonResponse
from Payment.models import FeaturePay

# Create your views here.

def charts(request):
    return render(request , 'charts/detail.html')

def chart_data(request):
    payments = FeaturePay.objects.all()
    data = []
    for payment in payments:
        data.append({
            'price': payment.price,
            'user': payment.user.username,
            'feature_name': payment.ticket.name,
            'date': payment.date
        })
    return JsonResponse({'data': data})