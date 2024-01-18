from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('add/', views.add, name='add'),

    #path('<slug:slug>', views.sale_orders, name='sales'),
    path('sales/', views.sales, name='sales'),
    path('dash/', views.dash, name='dash'),
    path("chart/filter-options/", views.get_filter_options, name="chart-filter-options"),
    path("chart/sales/<int:year>/", views.get_sales_chart, name="chart-sales"),
    path("chart/spend-per-customer/<int:year>/", views.spend_per_customer_chart, name="chart-spend-per-customer"),
    #path('generateinvoice/<int:pk>/', views.GenerateInvoice.as_view(), name = 'generateinvoice')
]