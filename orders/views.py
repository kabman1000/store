from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
import sys
from django.contrib import messages
# for generating pdf invoice
from django.utils import timezone
import datetime
from django.shortcuts import get_object_or_404
from .forms import StockHistorySearchForm
from django.contrib.auth.decorators import login_required

from basket.basket import Basket
from store.models import Product
from .models import Order, OrderItem


def payment_confirmation(order_number):
    Order.objects.filter(order_number=order_number).update(billing_status=True)
    print(order_number)


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_number = request.POST.get('order_number')
        user_id = request.user.id
        baskettotal = basket.get_total_price()
        full_name = request.POST.get('cusName')
        address1 = request.POST.get('add')
        phone = request.POST.get('phone_num')
        # Check if order exists
        if Order.objects.filter(order_number=order_number).exists():
            pass
        else:
            #print(order_number)
            order = Order.objects.create(user_id=user_id, full_name=full_name, address1=address1, phone=phone,total_paid=baskettotal, order_number=order_number)
            payment_confirmation(order_number)
            order_id = order.pk

            for item in basket:
                quant = item['qty']
                product_id = item['product'].id
                inv = Product.objects.get(id=product_id)
                #print(inv)
                print(inv.has_inventory())
                if inv.has_inventory():
                    inv.remove_items_from_inventory(count=quant)
                    OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])
                else:
                    messages.error(request, f'{inv} is out of stock')

        response = JsonResponse({'success': 'Return something'})
        return response


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders

@login_required
def sales(request):
    user_id = request.user.id
    sales = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    form = StockHistorySearchForm(request.POST or None)
    total = sum([sale.total_paid for sale in sales])
    print(total)
    if request.method == 'POST':
        sales = Order.objects.filter(user_id=user_id).filter(billing_status=True).filter(created__range=[form['start_date'].value(),form['end_date'].value()])
        total = sum([sale.total_paid for sale in sales])
    return render(request,
                  'account/user/sales.html', {'sales':sales, 'form':form, 'total':total})



    