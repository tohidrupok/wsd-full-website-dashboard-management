from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('banking', BankingAPI, basename='banking')
router.register('mobile-banking/', MobilelBankingAPI, basename='mobile-banking')

urlpatterns = [
    path('list/', order_list, name='order_list'),
    path('add-new-order/', add_new_order, name='add_new_order'),
    path('view-order/', view_order, name='view_order'),
    
    path('', include(router.urls)),
]