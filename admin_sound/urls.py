from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('admin-live-chat-sound', LiveChatAdminSoundAPI)

urlpatterns = [
    path('', include(router.urls)),
]