from django.urls import path
from .views import *

urlpatterns = [
    path('entrysound-API/', EntrySound_API.as_view(), name='EntrySound_API')
]