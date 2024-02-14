from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import EntrySound_Serializer

class EntrySound_API(generics.ListAPIView):
    queryset = EntrySound.objects.all()
    serializer_class = EntrySound_Serializer
