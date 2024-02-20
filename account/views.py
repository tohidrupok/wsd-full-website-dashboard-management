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
        'User List': reverse('user-list', request=request, format=format),
        'login': reverse('api-login', request=request, format=format),
        'login_otp_verification': reverse('api-login-otp-verify', request=request, format=format),
        
        'forget password': reverse('api-forget-password', request=request, format=format),
        'reset password': reverse('api-reset-password', request=request, format=format),
        
        'change password': reverse('change-password-api', request=request, format=format),
    })


class UserCreationAPI(generics.ListCreateAPIView):
    queryset = Custom_User.objects.all()
    serializer_class = UserCreationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Custom_User.objects.all()
    serializer_class = UserCreationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




# ==========User Login API Start==========
@api_view(['POST'])
def api_login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        otp = random.randint(111111, 999999)
            
        subject = 'OTP for Reset Password!'
        message = f'''Dear User,
        Email : {email}
        Your OTP is : {otp}'''
        from_email = settings.EMAIL_HOST_USER
        recipient_list=[email]
        send_mail(subject, message, from_email, recipient_list)
        
        request.session['login_otp'] = otp
        request.session['login_email'] = email
        request.session['login_password'] = password
        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def api_login_otp_verify(request):
    print('asdf', request.content_type)
    serializer = OTPVerificationSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        login_email = request.session.get('login_email')
        login_password = request.session.get('login_password')
        user = authenticate(email=login_email, password=login_password)
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==========User Login API End==========


# ==========Password Reset API Views Start==========
class ForgetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ForgetPasswordSerializer(data=request.data)
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
            
            request.session['reset_password_otp'] = otp
            request.session['reset_password_email'] = email
            return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = get_object_or_404(Custom_User, email=request.session.get('reset_password_email'))
            new_password = serializer.validated_data['password1']
            user.set_password(new_password)
            user.save()
            request.session['reset_password_otp'] = ''
            request.session['reset_password_email'] = ''
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==========Password Reset API Views End==========


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







# Dashboard Interface Function =====================
def dashboard(request):
    return render(request, 'dashboard.html')


# Logout Function ===================================
@login_required
def Logout(request):
    logout(request)
    return redirect('dashboard')


def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            token = default_token_generator.make_token(user)
            return redirect('login', token=token)
        else:
            messages.warning(request, form.errors)
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'admin_account/registration.html', {'form': form})



# Login Interface Function ==========================
def Login(request, token):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()
    if request.method == 'POST':
        
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            if not default_token_generator.check_token(get_object_or_404(Custom_User, email=email), token):
                messages.warning(request, 'This login url is not for you!')
                return redirect(request.META['HTTP_REFERER'])
            
            password = form.cleaned_data['password']
            otp = random.randint(111111, 999999)
            
            subject = 'OTP for Reset Password!'
            message = f'''Dear User,
            Email : {email}
            Your OTP is : {otp}'''
            from_email = settings.EMAIL_HOST_USER
            recipient_list=[email]
            send_mail(subject, message, from_email, recipient_list)
            
            request.session['login_otp'] = otp
            request.session['login_email'] = email
            request.session['login_password'] = password
            
            otp_form = OTPVerificationForm()
            context = {'otp_form': otp_form}
            return render(request,'admin_account/login/login_verify.html', context)
        else:
            messages.warning(request, form.errors)
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'admin_account/login/login.html', {'form': form})

def login_otp_verify(request):
    if request.method == 'POST':
        otp_form = OTPVerificationForm(request.POST, request=request)
        if otp_form.is_valid():
            login_email = request.session.get('login_email')
            login_password = request.session.get('login_password')
            user = authenticate(email=login_email, password=login_password)
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse(otp_form.errors)


# Forget Password Interface Function ===================
def forget_password(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = random.randint(111111, 999999)
            subject = 'OTP for Reset Password!'
            message = f'''Dear User,
            Email : {email}
            Your OTP is : {otp}'''
            from_email = settings.EMAIL_HOST_USER
            recipient_list=[email]
            
            send_mail(subject, message, from_email, recipient_list)
            
            request.session['reset_password_otp'] = otp
            request.session['reset_password_email'] = email
            return redirect('reset_password')
    else:
        form = ForgetPasswordForm()
    return render(request, 'admin_account/forget_password/forget_password.html', {'form': form})

# Reset Password Interface Function ===================
def reset_password(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(Custom_User, email=request.session.get('reset_password_email'))
            stored_otp = request.session.get('reset_password_otp')
            otp = int(form.cleaned_data['otp'])
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if otp == stored_otp:
                if password1 == password2:
                    user.set_password(password1)
                    user.save()
                    request.session['reset_password_otp'] = ''
                    return redirect('login')
                else:
                    messages.warning(request, "Password & Confirm Password Doesn't Match!")
            else:
                messages.warning(request, "OTP Doesn't Match!")
    else:
        form = ResetPasswordForm()
    return render(request, 'admin_account/forget_password/reset_password.html', {'form': form})


# Change Password Interface Function ===================
@login_required
def change_password(request):
    form = ChangePasswordForm(request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password change successfully !')
            return redirect('dashboard')
        else:
            messages.warning(request, form.errors)
            return redirect(request.META['HTTP_REFERER'])
    
    return render(request, 'admin_account/password_change.html', {'form': form})


