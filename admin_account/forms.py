from django import forms
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from .models import Custom_User

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='New Confirm Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email Address', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AdminUserAddForm(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['name', 'username', 'email', 'user_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=150, label='Email Address', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Email Address'
    }))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Custom_User.objects.filter(email=email).exists():
            None
        else:
            raise forms.ValidationError("Email does not exist in our database.")

        return email
    
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
    
