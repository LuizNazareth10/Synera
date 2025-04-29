from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from client.models import Client, Orders
from client.forms import ClientForm

def index(request):
    clients = Client.objects.all()
    return render(request, 'client/index.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client/client_detail.html', {'client': client})

def client_create(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('client:index')
        else:
            return render(request, 'client/client_form.html', {'client_form': client_form})
    else:
        client_form = ClientForm()
        return render(request, 'client/client_form.html', {'client_form': client_form})