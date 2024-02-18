from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('sound-list', Sound_API)
router.register('Admin-Call-Ringtone-API', Admin_Call_Ringtone_API)
router.register('admin-chat-notification-sound', Admin_Chat_Notification_Sound_API)
router.register('order-call-ringtone', Order_Call_Ringtone_API)
router.register('order-chat-notification-tone', Order_Chat_Notification_Tone_API)
router.register('user-cannot-call-admin-sound', User_Cannot_Call_Admin_Sound_API)
router.register('live-call-ringtone', Live_Call_Ringtone_API)
router.register('live-chat-notification-sound', Live_Chat_Notification_Sound_API)
router.register('live-chat-turned-off-sound', Live_Chat_Turned_Off_Sound_API)
router.register('live-chat-talk-sound', Live_Chat_Talk_Sound_API)
router.register('entrysound', EntrySound_API)

urlpatterns = [
    path('', include(router.urls)),
]