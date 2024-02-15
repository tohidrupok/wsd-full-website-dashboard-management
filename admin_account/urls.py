from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/', reset_password, name='reset_password'),
    
    path('profile/<username>/', user_profile, name='user_profile'),
    path('change-password/', change_password, name='change_password'),
    
    path('add-user/', add_update_user, name='add_user'),
    path('update-user/<int:id>/', add_update_user, name='update_user'),
    path('delete-user/<int:id>/', user_delete, name='user_delete'),
    path('user-list/', user_list, name='user_list'),
]