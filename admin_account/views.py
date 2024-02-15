from django.shortcuts import render, redirect, get_object_or_404
from user_management.forms import AdminUserAddForm
from .forms import ChangePasswordForm, LoginForm
from .models import Custom_User
from django.contrib.auth import login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def Logout(request):
    logout(request)
    return redirect('login')

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

@login_required
def user_profile(request, username):
    admin_user = get_object_or_404(Custom_User, username=username)
    return render(request, 'admin_account/user_profile.html', {'admin_user': admin_user})

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



