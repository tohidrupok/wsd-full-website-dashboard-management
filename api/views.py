from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

"""====== Start_Bank/Mobilewallet_Api_View ======"""
class BankCreateit(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializerit

class BankUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializerit

class MobileWalletCreateit(generics.ListCreateAPIView):
    queryset = MobileWallet.objects.all()
    serializer_class = MobileWalletSerializerit

class MobileWalletUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = MobileWallet.objects.all()
    serializer_class = MobileWalletSerializerit

"""====== End_Bank/Mobilewallet_Api_View ======"""


"""====== Start_OfflineBank/Mobilewallet_Api_View ======"""
class OfflineBankCreateit(generics.ListCreateAPIView):
    queryset = OfflineBank.objects.all()
    serializer_class = OfflineBankSerializerit

class OfflineBankUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfflineBank.objects.all()
    serializer_class = OfflineBankSerializerit

"""====== End_OfflineBank/Mobilewallet_Api_View ======"""


