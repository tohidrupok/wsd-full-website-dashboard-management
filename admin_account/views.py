from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Custom_User
from order.models import Order
from django.contrib.auth import login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import random
import string
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Dashboard Interface Function =====================
@login_required(login_url='login')
def dashboard(request):
    permission = Permission.objects.all()
    group = Group.objects.all()
    print('================Permision==============')
    print(permission)
    
    print('================Group==============')
    print(group)
    return render(request, 'dashboard.html')


# Logout Function ===================================
@login_required
def Logout(request):
    logout(request)
    return redirect('login')

# Login Interface Function ==========================
def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
        else:
            messages.warning(request, form.errors)
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'admin_account/login.html', {'form': form})

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



# User Profile Interface Function ===================
@login_required
def user_profile(request, username):
    admin_user = get_object_or_404(Custom_User, username=username)
    return render(request, 'admin_account/user_profile.html', {'admin_user': admin_user})

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


# Dashboard User List Interface Function ===================
@login_required
def user_list(request):
    if request.user.user_type != 'Admin':
        return redirect('dashboard')
    
    user_list = Custom_User.objects.all()
    return render(request, 'admin_account/user_list.html', {'user_list': user_list})

# Add or Update User Interface Function ===================
@login_required
def add_update_user(request, id=None):
    if request.user.user_type != 'Admin':
        return redirect('dashboard')
    # content_type = ContentType.objects.get_for_model(Order)
    # group = Group.objects.all()
    # print(group)
    # user_permission = Permission.objects.filter(content_type=content_type)
    # for i in user_permission:
    #     print(i)
    
    context = {}
    if id is not None:
        admin_user = get_object_or_404(Custom_User, id=id)
        form = AdminUserAddForm(instance=admin_user)
        context['form'] = form
        context['admin_user'] = admin_user
    else:
        form = AdminUserAddForm()
        context['form'] = form
    
    if request.method == 'POST':
        if id is not None:
            form = AdminUserAddForm(request.POST, instance=admin_user)
            if form.is_valid():
                form.save()
                messages.success(request, 'User Info Update!')
                return redirect('user_profile', username=request.user.username)
            else:
                messages.warning(request, form.errors)
                return redirect(request.META['HTTP_REFERER'])
        
        else:
            form = AdminUserAddForm(request.POST)
            if form.is_valid():
                user = form.save()
                random_password = ''.join(random.choice(string.ascii_letters) for i in range(10))
                print(random_password)
                user.set_password(random_password)
                user.save()
                
                subject = 'Congratulations for joined our Dashboard Panel!'
                message = f'''Dear {user.name},
                Your Email Address : {user.email}
                Your Username : {user.username}
                Your Password is : {user.password}'''
                from_email = settings.EMAIL_HOST_USER
                recipient_list=[user.email]
                
                send_mail(subject, message, from_email, recipient_list)
                
                messages.success(request, 'New User Added!')
                return redirect('user_list')
            else:
                messages.warning(request, form.errors)
                return redirect(request.META['HTTP_REFERER'])
        
    return render(request, 'admin_account/user_add.html', context)

# Delete User Function ===================================
@login_required
def user_delete(request, id):
    if request.user.user_type != 'Admin':
        return redirect('dashboard')
    
    admin_user = get_object_or_404(Custom_User, id=id)
    admin_user.delete()
    return redirect('user_list')
