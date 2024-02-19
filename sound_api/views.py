from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# User_Sound Model API Views==================================
class UserSoundAPI(viewsets.ModelViewSet):
    queryset = User_Sound.objects.all()
    serializer_class = UserSoundSerializer



# User_Order_Sound Model API Views==================================
class UserOrderSoundAPI(viewsets.ModelViewSet):
    queryset = User_Order_Sound.objects.all()
    serializer_class = UserOrderSoundSerializer


# Live_Chat_Admin Model API Views==================================
class LiveChatAdminSoundAPI(viewsets.ModelViewSet):
    queryset = Live_Chat_Admin_Sound.objects.all()
    serializer_class = LiveChatAdminSoundSerializer






