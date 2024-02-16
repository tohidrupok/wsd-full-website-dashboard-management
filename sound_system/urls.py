from django.urls import path, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', api_root, name='api_root'),
    
    # Sound Model API URL==================================
    path('sounds/', Sound_API.as_view(), name='sound_list'),
    path('sounds/<int:pk>/', SoundDetailAPI.as_view(), name='sound_detail'),
    
    
    # EntrySound Model API URL==================================
    path('entrysound/', EntrySound_API.as_view(), name='EntrySound_API'),
    path('entrysound/<int:pk>/', EntrySound_Detail_API.as_view(), name='EntrySound_Detail_API'),
    
    
    # Live_Chat_Talk_Sound Model API URL==================================
    path('live-chat-talk-sound/', Live_Chat_Talk_Sound_API.as_view(), name='Live_Chat_Talk_Sound_API'),
    path('live-chat-talk-sound/<int:pk>/', Live_Chat_Talk_Sound_Detail_API.as_view(), name='Live_Chat_Talk_Sound_Detail_API'),
    
    
    # Live_Chat_Turned_Off_Sound Model API URL==================================
    path('live-chat-turned-off-sound/', Live_Chat_Turned_Off_Sound_API.as_view(), name='Live_Chat_Turned_Off_Sound_API'),
    path('live-chat-turned-off-sound/<int:pk>/', Live_Chat_Turned_Off_Sound_Detail_API.as_view(), name='Live_Chat_Turned_Off_Sound_Detail_API'),
    
    
    # Live_Chat_Notification_Sound Model API URL==================================
    path('live-chat-notification-sound/', Live_Chat_Notification_Sound_API.as_view(), name='Live_Chat_Notification_Sound_API'),
    path('live-chat-notification-sound/<int:pk>/', Live_Chat_Notification_Sound_Detail_API.as_view(), name='Live_Chat_Notification_Sound_Detail_API'),
    
    # Live_Call_Ringtone Model API URL==================================
    path('Live_Call_Ringtone/', Live_Call_Ringtone_API.as_view(), name='Live_Call_Ringtone_API'),
    path('Live_Call_Ringtone/<int:pk>/', Live_Call_Ringtone_Detail_API.as_view(), name='Live_Call_Ringtone_Detail_API'),
    
    
    # User_Cannot_Call_Admin_Sound Model API URL==================================
    path('user-cannot-call-admin-sound/', User_Cannot_Call_Admin_Sound_API.as_view(), name='User_Cannot_Call_Admin_Sound_API'),
    path('user-cannot-call-admin-sound/<int:pk>/', User_Cannot_Call_Admin_Sound_Detail_API.as_view(), name='User_Cannot_Call_Admin_Sound_Detail_API'),
    
    # Order_Chat_Notification_Tone Model API URL==================================
    path('order-chat-notification-tone/', Order_Chat_Notification_Tone_API.as_view(), name='Order_Chat_Notification_Tone_API'),
    path('order-chat-notification-tone/<int:pk>/', Order_Chat_Notification_Tone_Detail_API.as_view(), name='Order_Chat_Notification_Tone_Detail_API'),
    
    # Order_Chat_Notification_Tone Model API URL==================================
    path('order-call-ringtone/', Order_Call_Ringtone_API.as_view(), name='Order_Call_Ringtone_API'),
    path('order-call-ringtone/<int:pk>/', Order_Call_Ringtone_Detail_API.as_view(), name='Order_Call_Ringtone_Detail_API'),
    
    
    # Admin_Chat_Notification_Sound Model API URL==================================
    path('admin-chat-notification-sound/', Admin_Chat_Notification_Sound_API.as_view(), name='Admin_Chat_Notification_Sound_API'),
    path('admin-chat-notification-sound/<int:pk>/', Admin_Chat_Notification_Sound_Detail_API.as_view(), name='Admin_Chat_Notification_Sound_Detail_API'),
    
    
    # Admin_Call_Ringtone Model API URL==================================
    path('admin-call-ringtone/', Admin_Call_Ringtone_API.as_view(), name='Admin_Call_Ringtone_List_API'),
    path('admin-call-ringtone/<int:pk>/', Admin_Call_Ringtone_Detail_API.as_view(), name='Admin_Call_Ringtone_Detail_API'),
    
])