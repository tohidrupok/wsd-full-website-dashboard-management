from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Order_Form
from .models import Order, Payment
from rest_framework import generics
from .serializer import Payment_Serializer


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})

def add_new_order(request):
    if request.method == 'POST':
        form = Order_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        else:
            messages.warning(request, form.errors)
    else:
        form = Order_Form()
    return render(request, 'order/add_order.html', {'form': form})

def view_order(request):
    return render(request, 'order/view_order.html')


class PaymentAPI(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = Payment_Serializer
class PaymentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = Payment_Serializer

