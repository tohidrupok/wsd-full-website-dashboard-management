from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserCreationAPI)
router.register(r'userprofiles', UserProfileAPI, basename='userprofile')
router.register(r'social-link', SocialLinkAPI)
router.register(r'conpany-information', CompanyInformationAPI)
router.register(r'contact-information', ContactInformationAPI)
router.register(r'address', AddressAPI)

urlpatterns = [
    path('', include(router.urls)),
    
    # User Change Password Api Url====================================
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password-api'),
    
    # User Login Api Url====================================
    path('login/', LoginAPI.as_view(), name='login-api'),
    
    # User Forget & Reset Password Api Url====================================
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='api-forget-password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='api-reset-password'),
    
    # User Verification Api Url====================================
    path('user-verification/', UserVerificationAPI.as_view(), name='api-account-verification'),
]

