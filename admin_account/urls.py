from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    
    path('change-password/', change_password, name='change_password')
]