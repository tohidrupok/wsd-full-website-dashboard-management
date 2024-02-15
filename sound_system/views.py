from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

def api_view_point_list(request):
    return render(request, 'api_view_poin_list.html')


class EntrySound_API(generics.ListCreateAPIView):
    queryset = EntrySound.objects.all()
    serializer_class = EntrySound_Serializer


class Live_Chat_Talk_Sound_API(generics.ListCreateAPIView):
    queryset = Live_Chat_Talk_Sound.objects.all()
    serializer_class = Live_Chat_Talk_Sound_Serializer


class Live_Chat_Turned_Off_Sound_API(generics.ListCreateAPIView):
    queryset = Live_Chat_Turned_Off_Sound.objects.all()
    serializer_class = Live_Chat_Turned_Off_Sound_Serializer


class Live_Chat_Notification_Sound_API(generics.ListCreateAPIView):
    queryset = Live_Chat_Notification_Sound.objects.all()
    serializer_class = Live_Chat_Notification_Sound_Serializer


class Live_Call_Ringtone_API(generics.ListCreateAPIView):
    queryset = Live_Call_Ringtone.objects.all()
    serializer_class = Live_Call_Ringtone_Serializer

class User_Cannot_Call_Admin_Sound_API(generics.ListCreateAPIView):
    queryset = User_Cannot_Call_Admin_Sound.objects.all()
    serializer_class = User_Cannot_Call_Admin_Sound_Serializer


class Order_Chat_Notification_Tone_API(generics.ListCreateAPIView):
    queryset = Order_Chat_Notification_Tone.objects.all()
    serializer_class = Order_Chat_Notification_Tone_Serializer


class Order_Call_Ringtone_API(generics.ListCreateAPIView):
    queryset = Order_Call_Ringtone.objects.all()
    serializer_class = Order_Call_Ringtone_Serializer


class Admin_Chat_Notification_Sound_API(generics.ListCreateAPIView):
    queryset = Admin_Chat_Notification_Sound.objects.all()
    serializer_class = Admin_Chat_Notification_Sound_Serializer


class Admin_Call_Ringtone_API(generics.ListCreateAPIView):
    queryset = Admin_Call_Ringtone.objects.all()
    serializer_class = Admin_Call_Ringtone_Serializer




class Sound_API(generics.ListCreateAPIView):
    queryset = Sound.objects.all()
    serializer_class = Sound_Serializer


