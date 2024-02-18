from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class OrderAPI(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Order_Work_DocumentAPI(viewsets.ModelViewSet):
    queryset = Order_Work_Document.objects.all()
    serializer_class = Order_Work_DocumentSerializer


class OrderAdminNoteAPI(viewsets.ModelViewSet):
    queryset = OrderAdminNote.objects.all()
    serializer_class = OrderAdminNoteSerializer


class Order_Update_BoxAPI(viewsets.ModelViewSet):
    queryset = Order_Update_Box.objects.all()
    serializer_class = Order_Update_BoxSerializer



