from django.contrib import admin
from .models import *

@admin.register(Order)
class Order_Admin(admin.ModelAdmin):
    list_display = ['product_title', 'product_price', 'quantity', 'status', 'order_date', 'update_date']
    list_filter = ['order_date', 'update_date']
    search_fields = ['product_title', 'product_price', 'quantity', 'status']

admin.site.register(Bank_Payment)
admin.site.register(Mobile_Banking_Payment)