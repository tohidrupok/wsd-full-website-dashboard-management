from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('message-topics', MessageTopicAPI)
router.register('message', MessageAPI)

urlpatterns = [
    path('', include(router.urls)),
]