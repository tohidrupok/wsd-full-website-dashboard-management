from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('creation', UserCreationAPI)
# router.register(r'your-model', YourModelViewSet)

urlpatterns = [
    path('user-list/', include(router.urls)),
    
    path('user/', api_root, name='api-root'),
    
    # User Login Api Url====================================
    path('user/login/', api_login, name='api-login'),
    path('user/login/otp-verify/', api_login_otp_verify, name='api-login-otp-verify'),
    
    # User Forget & Reset Password Api Url====================================
    path('user/forget-password/', ForgetPasswordAPIView.as_view(), name='api-forget-password'),
    path('user/reset-password/', ResetPasswordAPIView.as_view(), name='api-reset-password'),
    
    # User Change Password Api Url====================================
    path('user/change-password/', ChangePasswordAPIView.as_view(), name='change-password-api'),
    
    
    
    
    
    path('dashboard/', dashboard, name='dashboard'),
    
    path('registration/', registration, name='registration'),
    path('login/<token>/', Login, name='login'),
    path('login-verify/', login_otp_verify, name='login_verify'),
    
    path('logout/', Logout, name='logout'),
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/', reset_password, name='reset_password'),
    
    path('change-password/', change_password, name='change_password'),
    
]
