from django.shortcuts import render
from django.http import HttpResponse
from client.models import Client, Orders

def index(request):
    return render(request, 'client/index.html')