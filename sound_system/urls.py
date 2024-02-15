from django.urls import path
from .views import *

urlpatterns = [
    path('api-view-point/', api_view_point_list, name='api_view_point'),
    
    path('entrysound-API/', EntrySound_API.as_view(), name='EntrySound_API'),
    
    path('live-chat-talk-sound-API/', Live_Chat_Talk_Sound_API.as_view(), name='Live_Chat_Talk_Sound_API'),
    path('live-chat-turned-off-sound-API/', Live_Chat_Turned_Off_Sound_API.as_view(), name='Live_Chat_Turned_Off_Sound_API'),
    path('live-chat-notification-sound-API/', Live_Chat_Notification_Sound_API.as_view(), name='Live_Chat_Notification_Sound_API'),
    path('Live_Call_Ringtone-API/', Live_Call_Ringtone_API.as_view(), name='Live_Call_Ringtone_API'),
    path('user-cannot-call-admin-sound-API/', User_Cannot_Call_Admin_Sound_API.as_view(), name='User_Cannot_Call_Admin_Sound_API'),
    
    path('order-chat-notification-tone-API/', Order_Chat_Notification_Tone_API.as_view(), name='Order_Chat_Notification_Tone_API'),
    path('order-call-ringtone-API/', Order_Call_Ringtone_API.as_view(), name='Order_Call_Ringtone_API'),
    
    path('admin-chat-notification-sound-API/', Admin_Chat_Notification_Sound_API.as_view(), name='Admin_Chat_Notification_Sound_API'),
    path('admin-call-ringtone-API/', Admin_Call_Ringtone_API.as_view(), name='Admin_Call_Ringtone_API'),
    
    path('sound-API/', Sound_API.as_view(), name='Sound_API'),
]