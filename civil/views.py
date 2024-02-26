from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class Civil_OrderAPI(viewsets.ModelViewSet):
    queryset = Civil_Order.objects.all()
    serializer_class = Civil_OrderSerializer

class Civil_Order_Work_DocumentAPI(viewsets.ModelViewSet):
    queryset = Civil_Order_Work_Document.objects.all()
    serializer_class = Civil_Order_Work_DocumentSerializer


class Civil_OrderAdminNoteAPI(viewsets.ModelViewSet):
    queryset = Civil_Order_Admin_Note.objects.all()
    serializer_class = Civil_OrderAdminNoteSerializer


class Civil_Order_Update_BoxAPI(viewsets.ModelViewSet):
    queryset = Civil_Order_Update_Box.objects.all()
    serializer_class = Civil_Order_Update_BoxSerializer


class Civil_Order_User_Information_API(viewsets.ModelViewSet):
    queryset = Civil_Order_User_Information.objects.all()
    serializer_class = Civil_Order_User_Information_Serializer


class Civil_Order_Product_API(viewsets.ModelViewSet):
    queryset = Civil_Order_Product.objects.all()
    serializer_class = Civil_Order_Product_Serializer




# ==================================================
# Civil Order Payment Views Section Start
# ==================================================
# views.py
class CivilPaymentViewSet(viewsets.ModelViewSet):
    queryset = Civil_Payment.objects.all()
    serializer_class = CivilPaymentSerializer

class CivilBankPaymentViewSet(viewsets.ModelViewSet):
    queryset = Civil_BankPayment.objects.all()
    serializer_class = CivilBankPaymentSerializer

class CivilMobilePaymentViewSet(viewsets.ModelViewSet):
    queryset = Civil_MobilePayment.objects.all()
    serializer_class = CivilMobilePaymentSerializer

class CivilOfflinePaymentViewSet(viewsets.ModelViewSet):
    queryset = Civil_OfflinePayment.objects.all()
    serializer_class = CivilOfflinePaymentSerializer

# ==================================================
# Civil Order Payment Views Section End
# ==================================================



# ==================================================
# Civil Order Refund Views Section Start
# ==================================================
class CivilRefundViewSet(viewsets.ModelViewSet):
    queryset = Civil_Refund.objects.all()
    serializer_class = CivilRefundSerializer

class CivilBankRefundViewSet(viewsets.ModelViewSet):
    queryset = Civil_Bank_Refund.objects.all()
    serializer_class = CivilBankRefundSerializer

class CivilMobileRefundViewSet(viewsets.ModelViewSet):
    queryset = Civil_Mobile_Refund.objects.all()
    serializer_class = CivilMobileRefundSerializer
# ==================================================
# Civil Order Refund Views Section End
# ==================================================



