from django.shortcuts import render
from order.models import Order
from django.db.models import Q
from django.core.paginator import Paginator
from order.forms import OrderForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        orders = Order.objects.filter(Q(pk__icontains=search_query)|Q(name=search_query)).order_by('-id')
    else:
        orders = Order.objects.all().order_by('-id')

    paginator = Paginator(orders, 10)  # Show 10 orders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'orders': page_obj,
        'search_query': search_query,
        # 'page_obj': page_obj,
    }
    
    return render(request, 'order/index.html', context)

def order_create(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('order:index')
        else:
            context = {
                'order_form': order_form,
            }
            return render(request, 'order/order_form.html', context)
            # return render(request, 'order/order_form.html', {'order_form': order_form})
    else:
        order_form = OrderForm()
        context = {
            'order_form': order_form,
        }
        return render(request, 'order/order_form.html', context)
        # return render(request, 'order/order_form.html', {'order_form': order_form})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})