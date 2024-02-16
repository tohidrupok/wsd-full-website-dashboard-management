from django.urls import path
from .views import *

urlpatterns = [
    path('', order_list, name='order_list'),
    path('add-new-order/', add_new_order, name='add_new_order'),
    path('view-order/', view_order, name='view_order'),
    
    path('api/payment/', PaymentAPI.as_view(), name='PaymentAPI'),
    path('api/payment/<int:pk>/', PaymentDetailAPI.as_view(), name='PaymentDetailAPI'),
]