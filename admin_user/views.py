from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import *
from .serializers import *
from .forms import *
import random


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Admin User List': reverse('user-list', request=request, format=format),
        'admin login': reverse('api-admin-login', request=request, format=format),
        'admin login otp verification': reverse('admin-login-otp-verification', request=request, format=format),
        
        'admin forget password': reverse('api-admin-forget-password', request=request, format=format),
        'admin reset password': reverse('api-admin-reset-password', request=request, format=format),
        
        'admin change password': reverse('admin-change-password-api', request=request, format=format),
    })


class AdminUserCreationAPI(generics.ListCreateAPIView):
    queryset = Admin_User.objects.all()
    serializer_class = AdminUserCreationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AdminUserUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin_User.objects.all()
    serializer_class = AdminUserCreationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)




# ==========User Login API Start==========
@api_view(['POST'])
def admin_api_login(request, token=None):
    serializer = AdminLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        admin_user = Admin_User.objects.get(username=username)
        
        if admin_user.user_authentication.token == token:
            otp = random.randint(111111, 999999)
            subject = 'OTP for Login Your Account!'
            message = f'''Dear User,
            Email : {admin_user.email}
            Username : {admin_user.username}
            Your OTP is : {otp}'''
            from_email = settings.EMAIL_HOST_USER
            recipient_list=[admin_user.email]
            send_mail(subject, message, from_email, recipient_list)
            
            request.session['admin_login_otp'] = otp
            request.session['admin_login_email'] = admin_user.email
            request.session['admin_username'] = username
            request.session['admin_password'] = password
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
            
        else:
            return Response({'message': 'Invalid Token!'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def admin_api_login_otp_verify(request):
    serializer = AdminOTPVerificationSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        admin_login_email = request.session.get('admin_login_email')
        admin_login_username = request.session.get('admin_username')
        admin_login_password = request.session.get('admin_password')
        email = serializer.validated_data['email']
        if admin_login_email != email:
            return Response({'message': 'Wrong Email Address!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = authenticate(username=admin_login_username, password=admin_login_password)
            login(request, user)
            request.session['admin_login_otp'] = ''
            request.session['admin_login_email'] = ''
            request.session['admin_username'] = ''
            request.session['admin_password'] = ''
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==========User Login API End==========




# ==========Password Reset API Views Start==========
class AdminForgetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdminForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = random.randint(111111, 999999)
            subject = 'OTP for Reset Password!'
            message = f'''Dear User,
            Email : {email}
            Your OTP is : {otp}'''
            from_email = settings.EMAIL_HOST_USER
            recipient_list=[email]
            
            send_mail(subject, message, from_email, recipient_list)
            
            request.session['admin_reset_password_otp'] = otp
            request.session['admin_reset_password_email'] = email
            return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminResetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdminResetPasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = get_object_or_404(Admin_User, email=request.session.get('admin_reset_password_email'))
            new_password = serializer.validated_data['password1']
            user.set_password(new_password)
            user.save()
            request.session['reset_password_otp'] = ''
            request.session['reset_password_email'] = ''
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==========Password Reset API Views End==========


# ==========Password Change API Views Start==========
class AdminChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = AdminChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            form = AdminChangePasswordForm(request.user, data=serializer.validated_data)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return Response({'detail': 'Password changed successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# ==========Password Change API Views End==========




