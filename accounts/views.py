from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'accounts/stonks.html')

def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def terms(request):
    return render(request, 'accounts/terms.html')

def client(request, ID):
    client = Client.objects.get(id = ID)
    stocks = client.client_stock_set.all()
    
    assets = 0
    for S in stocks:
        assets += (S.Shares*S.SID.Price)

    context = {'client': client, 'stocks': stocks, 'assets': assets}
    return render(request, 'accounts/client.html', context)

def broker(request, ID):
    broker = Broker.objects.get(id = ID)
    clients = broker.client_broker_set.all()
    cnt_cli = broker.client_broker_set.all().count()
    
    for C in clients:
        cr = C.CID.id
        stocks = Stock.objects.get(id = cr)

    context = {'broker': broker, 'clients': clients, "cnt_cli": cnt_cli, 'stocks': stocks}
    return render(request, 'accounts/broker.html', context)