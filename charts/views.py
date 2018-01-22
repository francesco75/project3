from django.shortcuts import render
from django.http import JsonResponse
from Payment.models import FeaturePay
from ticket.models import Ticket
from vote.models import Vote
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
    return JsonResponse(data, safe=False)




def chart_vote(request):
    votes = Vote.objects.all()
    databug = []
    for vote in votes:
        databug.append({
            'ticket': vote.ticket_id,
            'user': vote.user_id,
            'ticket_type': vote.ticket.type,
            'ticket_name': vote.ticket.name,
            'ticket_date': vote.ticket.date
        })
    return JsonResponse(databug, safe=False)