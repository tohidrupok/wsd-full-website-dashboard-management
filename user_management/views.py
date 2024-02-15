from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdminUserAddForm
from django.contrib import messages
from admin_account.models import Custom_User
from django.contrib.auth.decorators import login_required
import random
import string

@login_required
def user_list(request):
    user_list = Custom_User.objects.all()
    return render(request, 'user_management/user_list.html', {'user_list': user_list})

@login_required
def add_update_user(request, id=None):
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
                result_str = ''.join(random.choice(string.ascii_letters) for i in range(10))
                user.set_password(result_str)
                user.save()
                messages.success(request, 'New User Added!')
                return redirect('user_list')
            else:
                messages.warning(request, form.errors)
                return redirect(request.META['HTTP_REFERER'])
        
    return render(request, 'user_management/user_add.html', context)


