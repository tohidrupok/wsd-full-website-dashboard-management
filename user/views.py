from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash
from .forms import ChangePasswordForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
import random


# ==============================
# Views For Website User Registration And Verficiation
# ==================================
class UserCreationAPI(viewsets.ModelViewSet):
    queryset = Website_User.objects.all()
    serializer_class = UserCreationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        otp = random.randint(111111, 999999)
        subject = 'OTP for Account Verification!'
        message = f'''Dear User,
        Email : {user.email}
        Your OTP is : {otp}'''
        from_email = settings.EMAIL_HOST_USER
        recipient_list=[user.email]
        
        send_mail(subject, message, from_email, recipient_list)
        
        request.session['account_verify_otp'] = otp
        request.session['account_verify_email'] = user.email
        return Response({'message': 'User Creation Successfully! Check Your Email For Verification!'})

class UserVerificationAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserVerificationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            email = request.session.get('account_verify_email')
            user = get_object_or_404(Website_User, email=email)
            
            user.is_varified = True
            user.save()
            return Response({'message': 'Your Account Verification Complete!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        serializer = UserVerificationSerializer()
        return Response(serializer.data)



# =============== Views For Website User Profile ===================
class UserProfileAPI(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# =========== Views For Website User Company Information ===============
class CompanyInformationAPI(viewsets.ModelViewSet):
    queryset = CompanyInformation.objects.all()
    serializer_class = CompanyInformationSerializer

# ========== Views For Website User Contact Information ==============
class ContactInformationAPI(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer

# ================ Views For Website User Social Link ====================
class SocialLinkAPI(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer

# ================= Views For Website User Address =====================
class AddressAPI(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer



# ==========Password Change API Views Start==========
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            form = ChangePasswordForm(request.user, data=serializer.validated_data)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return Response({'detail': 'Password changed successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# ==========Password Change API Views End==========


# ==========User Login API Start==========
class LoginAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return Response({'message': 'Login Successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==========User Login API End==========





# ==========Password Reset API Views Start==========
class ForgetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']
            otp = random.randint(111111, 999999)
            subject = 'OTP for Reset Password!'
            message = f'''Dear User,
            Email : {email}
            Your OTP is : {otp}'''
            from_email = settings.EMAIL_HOST_USER
            recipient_list=[email]
            
            send_mail(subject, message, from_email, recipient_list)
            
            request.session['user_reset_password_otp'] = otp
            request.session['user_reset_password_email'] = email
            request.session['user_reset_password_username'] = username
            return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = get_object_or_404(Website_User, email=request.session.get('user_reset_password_email'))
            new_password = serializer.validated_data['password1']
            user.set_password(new_password)
            user.save()
            
            request.session['reset_password_otp'] = ''
            request.session['reset_password_email'] = ''
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==========Password Reset API Views End==========




