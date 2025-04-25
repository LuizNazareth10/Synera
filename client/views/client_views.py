from django.shortcuts import render
from django.http import HttpResponse
from client.models import Client, Orders

def index(request):
    clients = Client.objects.all()
    return render(request, 'global/base.html', {'clients': clients})