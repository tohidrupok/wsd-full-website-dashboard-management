from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', OrderAPI)
router.register('order-work-document', Order_Work_DocumentAPI)
router.register('order-admin-note', OrderAdminNoteAPI)
router.register('order-update-box', Order_Update_BoxAPI)

urlpatterns = [
    path('', include(router.urls)),
]