from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Live_Chat_Admin Model API Views==================================
class LiveChatAdminSoundAPI(viewsets.ModelViewSet):
    queryset = Live_Chat_Admin_Sound.objects.all()
    serializer_class = LiveChatAdminSoundSerializer



