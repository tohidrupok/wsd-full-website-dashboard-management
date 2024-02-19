from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class MessageTopicAPI(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = MessageTopicSerializer


class MessageAPI(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer

