from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

order_router = DefaultRouter()
order_router.register(r'it_orders', IT_OrderAPI, basename='it_order')
order_router.register(r'it_order_work_documents', IT_Order_Work_DocumentAPI, basename='it_order_work_document')
order_router.register(r'it_order_admin_notes', IT_OrderAdminNoteAPI, basename='it_order_admin_note')
order_router.register(r'it_order_update_boxes', IT_Order_Update_BoxAPI, basename='it_order_update_box')
order_router.register(r'it_order_user_information', IT_Order_User_Information_API, basename='it_order_user_information')
order_router.register(r'it_order_products', IT_Order_Product_API, basename='it_order_product')


# ==================================================
# IT Order Payment urls Section Start
# ==================================================
payment_router = DefaultRouter()
payment_router.register(r'it_payments', ITPaymentViewSet)
payment_router.register(r'it_bank_payments', ITBankPaymentViewSet)
payment_router.register(r'it_mobile_payments', ITMobilePaymentViewSet)
payment_router.register(r'it_offline_payments', ITOfflinePaymentViewSet, basename='it_offline_payment')
# ==================================================
# IT Order Payment urls Section End
# ==================================================

# ==================================================
# IT Order Refund Models Section Start
# ==================================================
refund_router = DefaultRouter()
refund_router.register(r'it-refunds', ITRefundViewSet)
refund_router.register(r'it-bank-refunds', ITBankRefundViewSet)
refund_router.register(r'it-mobile-refunds', ITMobileRefundViewSet)
# ==================================================
# IT Order Refund Models Section End
# ==================================================

urlpatterns = [
    path('order/', include(order_router.urls)),
    path('payment/', include(payment_router.urls)),
    path('refund/', include(refund_router.urls)),
]
