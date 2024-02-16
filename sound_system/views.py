from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializer import *

# EntrySound Model API Serializer==================================
class EntrySound_API(generics.ListCreateAPIView):
    queryset = EntrySound.objects.all()
    serializer_class = EntrySound_Serializer

class EntrySound_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntrySound.objects.all()
    serializer_class = EntrySound_Serializer


# Live_Chat_Talk_Sound Model API Serializer==================================
class Live_Chat_Talk_Sound_API(generics.ListCreateAPIView):
    queryset = Live_Chat_Talk_Sound.objects.all()
    serializer_class = Live_Chat_Talk_Sound_Serializer

class Live_Chat_Talk_Sound_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Live_Chat_Talk_Sound.objects.all()
    serializer_class = Live_Chat_Talk_Sound_Serializer


# Live_Chat_Turned_Off_Sound Model API Serializer==================================
class Live_Chat_Turned_Off_Sound_API(generics.ListCreateAPIView):
    queryset = Live_Chat_Turned_Off_Sound.objects.all()
    serializer_class = Live_Chat_Turned_Off_Sound_Serializer

class Live_Chat_Turned_Off_Sound_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Live_Chat_Turned_Off_Sound.objects.all()
    serializer_class = Live_Chat_Turned_Off_Sound_Serializer


# Live_Chat_Notification_Sound Model API Serializer==================================
class Live_Chat_Notification_Sound_API(generics.ListCreateAPIView):
    queryset = Live_Chat_Notification_Sound.objects.all()
    serializer_class = Live_Chat_Notification_Sound_Serializer

class Live_Chat_Notification_Sound_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Live_Chat_Notification_Sound.objects.all()
    serializer_class = Live_Chat_Notification_Sound_Serializer

# Live_Call_Ringtone Model API Serializer==================================
class Live_Call_Ringtone_API(generics.ListCreateAPIView):
    queryset = Live_Call_Ringtone.objects.all()
    serializer_class = Live_Call_Ringtone_Serializer

class Live_Call_Ringtone_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Live_Call_Ringtone.objects.all()
    serializer_class = Live_Call_Ringtone_Serializer


# User_Cannot_Call_Admin_Sound Model API Serializer==================================
class User_Cannot_Call_Admin_Sound_API(generics.ListCreateAPIView):
    queryset = User_Cannot_Call_Admin_Sound.objects.all()
    serializer_class = User_Cannot_Call_Admin_Sound_Serializer

class User_Cannot_Call_Admin_Sound_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_Cannot_Call_Admin_Sound.objects.all()
    serializer_class = User_Cannot_Call_Admin_Sound_Serializer



# Order_Chat_Notification_Tone Model API Serializer==================================
class Order_Chat_Notification_Tone_API(generics.ListCreateAPIView):
    queryset = Order_Chat_Notification_Tone.objects.all()
    serializer_class = Order_Chat_Notification_Tone_Serializer

class Order_Chat_Notification_Tone_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order_Chat_Notification_Tone.objects.all()
    serializer_class = Order_Chat_Notification_Tone_Serializer


# Order_Chat_Notification_Tone Model API Serializer==================================
class Order_Call_Ringtone_API(generics.ListCreateAPIView):
    queryset = Order_Call_Ringtone.objects.all()
    serializer_class = Order_Call_Ringtone_Serializer

class Order_Call_Ringtone_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order_Call_Ringtone.objects.all()
    serializer_class = Order_Call_Ringtone_Serializer


# Admin_Chat_Notification_Sound Model API Serializer==================================
class Admin_Chat_Notification_Sound_API(generics.ListCreateAPIView):
    queryset = Admin_Chat_Notification_Sound.objects.all()
    serializer_class = Admin_Chat_Notification_Sound_Serializer

class Admin_Chat_Notification_Sound_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin_Chat_Notification_Sound.objects.all()
    serializer_class = Admin_Chat_Notification_Sound_Serializer


# Admin_Call_Ringtone Model API Serializer==================================
class Admin_Call_Ringtone_API(generics.ListCreateAPIView):
    queryset = Admin_Call_Ringtone.objects.all()
    serializer_class = Admin_Call_Ringtone_Serializer

class Admin_Call_Ringtone_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin_Call_Ringtone.objects.all()
    serializer_class = Admin_Call_Ringtone_Serializer


# Sound Model API Serializer==================================
class Sound_API(generics.ListCreateAPIView):
    queryset = Sound.objects.all()
    serializer_class = Sound_Serializer

class SoundDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sound.objects.all()
    serializer_class = Sound_Serializer






@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Sount List': reverse('sound_list', request=request, format=format),
        'EntrySound_API': reverse('EntrySound_API', request=request, format=format),
        
        'Live_Chat_Talk_Sound_API': reverse('Live_Chat_Talk_Sound_API', request=request, format=format),
        'Live_Chat_Turned_Off_Sound_API': reverse('Live_Chat_Turned_Off_Sound_API', request=request, format=format),
        'Live_Chat_Notification_Sound_API': reverse('Live_Chat_Notification_Sound_API', request=request, format=format),
        'Live_Call_Ringtone_API': reverse('Live_Call_Ringtone_API', request=request, format=format),
        'User_Cannot_Call_Admin_Sound_API': reverse('User_Cannot_Call_Admin_Sound_API', request=request, format=format),
        
        'Order_Chat_Notification_Tone_API': reverse('Order_Chat_Notification_Tone_API', request=request, format=format),
        'Order_Call_Ringtone_API': reverse('Order_Call_Ringtone_API', request=request, format=format),
        
        'Admin_Chat_Notification_Sound_API': reverse('Admin_Chat_Notification_Sound_API', request=request, format=format),
        
        'Admin Call Ringtone List': reverse('Admin_Call_Ringtone_List_API', request=request, format=format),
    })


