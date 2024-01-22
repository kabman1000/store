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
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse

from basket.basket import Basket
from store.models import Product
from .models import Order, OrderItem
from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict


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
    print(orders)
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

def dash(request):
    orders = Order.objects.all()
    order_items = OrderItem.objects.all()
    print(orders)
    print(order_items)
    return render(request,
                  'account/user/dashmoard.html', {'order_items':order_items, 'orders':orders})


def get_filter_options(request):
    grouped_purchases = Order.objects.annotate(year=ExtractYear("created")).values("year").order_by("-year").distinct()
    options = [purchase["year"] for purchase in grouped_purchases]

    return JsonResponse({
        "options": options,
    })


def get_sales_chart(request, year):
    purchases = Order.objects.filter(created__year=year)
    grouped_purchases = purchases.annotate(price=F("total_paid")).annotate(month=ExtractMonth("created"))\
        .values("month").annotate(average=Sum("total_paid")).values("month", "average").order_by("month")

    sales_dict = get_year_dict()

    for group in grouped_purchases:
        sales_dict[months[group["month"]-1]] = round(group["average"], 2)

    return JsonResponse({
        "title": f"Sales in {year}",
        "data": {
            "labels": list(sales_dict.keys()),
            "datasets": [{
                "label": "Amount (₵)",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(sales_dict.values()),
            }]
        },
    })


def spend_per_customer_chart(request, year):
    purchases = Order.objects.filter(created__year=year)
    grouped_purchases = purchases.annotate(price=F("total_paid")).annotate(month=ExtractMonth("created"))\
        .values("month").annotate(average=Avg("total_paid")).values("month", "average").order_by("month")

    spend_per_customer_dict = get_year_dict()

    for group in grouped_purchases:
        spend_per_customer_dict[months[group["month"]-1]] = round(group["average"], 2)

    return JsonResponse({
        "title": f"Spend per customer in {year}",
        "data": {
            "labels": list(spend_per_customer_dict.keys()),
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(spend_per_customer_dict.values()),
            }]
        },
    })


def statistics_view(request):
    return render(request, "account/user/statistics.html", {})

def get_most_sold_chart(request, year):
    purchases = Order.objects.filter(created__year=year)
    grouped_purchases = purchases.annotate(price=F("total_paid")).annotate(month=ExtractMonth("created"))\
        .values("month").annotate(average=Sum("total_paid")).values("month", "average").order_by("month")

    sales_dict = get_year_dict()

    for group in grouped_purchases:
        sales_dict[months[group["month"]-1]] = round(group["average"], 2)

    return JsonResponse({
        "title": f"Sales in {year}",
        "data": {
            "labels": list(sales_dict.keys()),
            "datasets": [{
                "label": "Amount (₵)",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(sales_dict.values()),
            }]
        },
    })