from django.urls import path, include
from .views import *

urlpatterns = [
    path('', api_root, name='api-root'),
    
    # User List And Create Api Url====================================
    path('user-list/', AdminUserCreationAPI.as_view(), name='user-list'),
    path('user-list/<int:pk>/', AdminUserUpdateDeleteAPI.as_view(), name='user'),
    
    # User Login Api Url====================================
    path('login/', admin_api_login, name='api-admin-login'),
    path('login/<token>/', admin_api_login, name='api-login-token'),
    path('login-verification/', admin_api_login_otp_verify, name='admin-login-otp-verification'),
    
    # User Forget & Reset Password Api Url====================================
    path('forget-password/', AdminForgetPasswordAPIView.as_view(), name='api-admin-forget-password'),
    path('reset-password/', AdminResetPasswordAPIView.as_view(), name='api-admin-reset-password'),
    
    # User Change Password Api Url====================================
    path('change-password/', AdminChangePasswordAPIView.as_view(), name='admin-change-password-api'),
    
]
