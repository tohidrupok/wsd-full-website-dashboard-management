from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class IT_OrderAPI(viewsets.ModelViewSet):
    queryset = IT_Order.objects.all()
    serializer_class = IT_OrderSerializer

class IT_Order_Work_DocumentAPI(viewsets.ModelViewSet):
    queryset = IT_Order_Work_Document.objects.all()
    serializer_class = IT_Order_Work_DocumentSerializer


class IT_OrderAdminNoteAPI(viewsets.ModelViewSet):
    queryset = IT_Order_Admin_Note.objects.all()
    serializer_class = IT_OrderAdminNoteSerializer


class IT_Order_Update_BoxAPI(viewsets.ModelViewSet):
    queryset = IT_Order_Update_Box.objects.all()
    serializer_class = IT_Order_Update_BoxSerializer


class IT_Order_User_Information_API(viewsets.ModelViewSet):
    queryset = IT_Order_User_Information.objects.all()
    serializer_class = IT_Order_User_Information_Serializer


class IT_Order_Product_API(viewsets.ModelViewSet):
    queryset = IT_Order_Product.objects.all()
    serializer_class = IT_Order_Product_Serializer




# ==================================================
# IT Order Payment Views Section Start
# ==================================================
class ITPaymentViewSet(viewsets.ModelViewSet):
    queryset = IT_Payment.objects.all()
    serializer_class = ITPaymentSerializer

class ITBankPaymentViewSet(viewsets.ModelViewSet):
    queryset = IT_BankPayment.objects.all()
    serializer_class = ITBankPaymentSerializer

class ITMobilePaymentViewSet(viewsets.ModelViewSet):
    queryset = IT_MobilePayment.objects.all()
    serializer_class = ITMobilePaymentSerializer
# ==================================================
# IT Order Payment Views Section End
# ==================================================

