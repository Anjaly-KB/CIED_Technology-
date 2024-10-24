# from django.shortcuts import render

# Create your views here.

# converter/views.py
import requests
from django.shortcuts import render, redirect
from .models import ConversionHistory

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def index(request):
    return render(request, 'index.html')

def convert_currency(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']

        response = requests.get(API_URL + from_currency)
        data = response.json()
        exchange_rate = data['rates'].get(to_currency)

        if exchange_rate:
            converted_amount = amount * exchange_rate
            
            # Save to history
            ConversionHistory.objects.create(
                amount=amount,
                from_currency=from_currency,
                to_currency=to_currency,
                converted_amount=converted_amount,
                conversion_rate=exchange_rate
            )
            
            return render(request, 'result.html', {
                'converted_amount': converted_amount,
                'exchange_rate': exchange_rate,
                'from_currency': from_currency,
                'to_currency': to_currency,
            })
    
    return redirect('index')

def conversion_history(request):
    history = ConversionHistory.objects.all().order_by('-timestamp')[:5]
    return render(request,'history.html',{'history':history})