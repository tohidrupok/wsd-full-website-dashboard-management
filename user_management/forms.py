from admin_account.models import Custom_User
from django import forms

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

