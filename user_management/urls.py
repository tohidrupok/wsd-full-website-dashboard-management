from django.urls import path
from .views import *

urlpatterns = [
    path('add-user/', add_update_user, name='add_user'),
    path('update-user/<int:id>/', add_update_user, name='update_user'),
    path('user-list/', user_list, name='user_list'),
]