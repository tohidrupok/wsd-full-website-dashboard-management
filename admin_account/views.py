from django.shortcuts import render, redirect
# from django.contrib.auth.forms import PasswordChangeForm
from .forms import ChangePasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def Logout(request):
    return redirect('login')

def Login(request):
    return redirect('login')

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
            messages.warning(request, 'Password change successfully!')
            return redirect(request.META['HTTP_REFERER'])
    
    return render(request, 'admin_account/password_change.html', {'form': form})

