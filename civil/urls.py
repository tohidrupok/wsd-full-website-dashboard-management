from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

order_router = DefaultRouter()
order_router.register(r'civil_orders', Civil_OrderAPI, basename='civil_order')
order_router.register(r'civil_order_work_documents', Civil_Order_Work_DocumentAPI, basename='civil_order_work_document')
order_router.register(r'civil_order_admin_notes', Civil_OrderAdminNoteAPI, basename='civil_order_admin_note')
order_router.register(r'civil_order_update_boxes', Civil_Order_Update_BoxAPI, basename='civil_order_update_box')
order_router.register(r'civil_order_user_information', Civil_Order_User_Information_API, basename='civil_order_user_information')
order_router.register(r'civil_order_products', Civil_Order_Product_API, basename='civil_order_product')


# ==================================================
# Civil Order Payment urls Section Start
# ==================================================
order_router.register(r'civil_payments', CivilPaymentViewSet)
order_router.register(r'civil_bank_payments', CivilBankPaymentViewSet)
order_router.register(r'civil_mobile_payments', CivilMobilePaymentViewSet)
# ==================================================
# Civil Order Payment urls Section End
# ==================================================

urlpatterns = [
    path('order/', include(order_router.urls)),
]
