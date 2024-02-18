from typing import Any
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm, PasswordResetForm
from .models import Custom_User

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='New Confirm Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email Address', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(label='OTP', max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OTPVerificationForm, self).__init__(*args, **kwargs)
    
    def clean_otp(self) -> dict[str, Any]:
        otp = int(self.cleaned_data['otp'])
        stored_otp = self.request.session.get('login_otp')
        if otp == stored_otp:
            return otp
        else:
            raise forms.ValidationError("OTP does not Match.")



class CreateUserForm(UserCreationForm):
    name = forms.CharField(max_length=50, label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.EmailField(max_length=50, label='Email Address', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    password2 = forms.CharField(max_length=50, label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    class Meta:
        model = Custom_User
        fields = ['name', 'email', 'username', 'user_type']
        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-control'})
        }



class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=150, label='Email Address', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Email Address'
    }))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Custom_User.objects.filter(email=email).exists():
            return email
        else:
            raise forms.ValidationError("Email does not exist in our database.")
    
class ResetPasswordForm(forms.Form):
    otp = forms.CharField(max_length=6, label='OTP', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(max_length=50, label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    
    
    
