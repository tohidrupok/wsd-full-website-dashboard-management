from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# EntrySound Model API Serializer==================================
class EntrySound_API(viewsets.ModelViewSet):
    queryset = EntrySound.objects.all()
    serializer_class = EntrySound_Serializer



# Live_Chat_Talk_Sound Model API Serializer==================================
class Live_Chat_Talk_Sound_API(viewsets.ModelViewSet):
    queryset = Live_Chat_Talk_Sound.objects.all()
    serializer_class = Live_Chat_Talk_Sound_Serializer


# Live_Chat_Turned_Off_Sound Model API Serializer==================================
class Live_Chat_Turned_Off_Sound_API(viewsets.ModelViewSet):
    queryset = Live_Chat_Turned_Off_Sound.objects.all()
    serializer_class = Live_Chat_Turned_Off_Sound_Serializer


# Live_Chat_Notification_Sound Model API Serializer==================================
class Live_Chat_Notification_Sound_API(viewsets.ModelViewSet):
    queryset = Live_Chat_Notification_Sound.objects.all()
    serializer_class = Live_Chat_Notification_Sound_Serializer


# Live_Call_Ringtone Model API Serializer==================================
class Live_Call_Ringtone_API(viewsets.ModelViewSet):
    queryset = Live_Call_Ringtone.objects.all()
    serializer_class = Live_Call_Ringtone_Serializer


# User_Cannot_Call_Admin_Sound Model API Serializer==================================
class User_Cannot_Call_Admin_Sound_API(viewsets.ModelViewSet):
    queryset = User_Cannot_Call_Admin_Sound.objects.all()
    serializer_class = User_Cannot_Call_Admin_Sound_Serializer


# Order_Chat_Notification_Tone Model API Serializer==================================
class Order_Chat_Notification_Tone_API(viewsets.ModelViewSet):
    queryset = Order_Chat_Notification_Tone.objects.all()
    serializer_class = Order_Chat_Notification_Tone_Serializer


# Order_Chat_Notification_Tone Model API Serializer==================================
class Order_Call_Ringtone_API(viewsets.ModelViewSet):
    queryset = Order_Call_Ringtone.objects.all()
    serializer_class = Order_Call_Ringtone_Serializer


# Admin_Chat_Notification_Sound Model API Serializer==================================
class Admin_Chat_Notification_Sound_API(viewsets.ModelViewSet):
    queryset = Admin_Chat_Notification_Sound.objects.all()
    serializer_class = Admin_Chat_Notification_Sound_Serializer


# Admin_Call_Ringtone Model API Serializer==================================
class Admin_Call_Ringtone_API(viewsets.ModelViewSet):
    queryset = Admin_Call_Ringtone.objects.all()
    serializer_class = Admin_Call_Ringtone_Serializer


# Sound Model API Serializer==================================
class Sound_API(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = Sound_Serializer




