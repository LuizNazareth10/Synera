from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from client.models import Client
from client.forms import ClientForm
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        # clients = Client.objects.filter(Q(name__icontains=search_query)| Q()).order_by('-id')
        clients = Client.objects.filter(Q(name__icontains=search_query) | Q(pk__icontains=search_query)).order_by('-id')
    else:
        clients = Client.objects.all().order_by('-id')
    # clients = Client.objects.order_by('-id')
    paginator = Paginator(clients, 10)  # Show 10 clients per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'clients': page_obj,
        'search_query': search_query,
        'page_obj': page_obj,

    }
    return render(request, 'client/index.html', context)

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