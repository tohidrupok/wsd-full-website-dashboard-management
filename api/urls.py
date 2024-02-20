from django.urls import path
from .views import *
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

   #======= Start_Bank/MobileWallet_api_url_ =======
    path('it/bank/', BankCreateit.as_view(), name='bank-create'),
    path('it/bank/<int:pk>/', BankUpdateit.as_view(), name='bank-detail'),
    path('it/mobilewallet/', MobileWalletCreateit.as_view(), name='mobileWallet-create'),
    path('it/mobilewallet/<int:pk>/', MobileWalletUpdateit.as_view(), name='mobileWallet-detail'),

   #======= Start_OfflineBank_api_url_ =======
    path('it/offlinebank/', OfflineBankCreateit.as_view(), name='offline-bank-create'),
    path('it/offlinebank/<int:pk>/', OfflineBankUpdateit.as_view(), name='offline-bank-detail'),
    
    
    
    
]
