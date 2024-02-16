from django import forms
from .models import *

class Update_Status(forms.Form):
    STATUS = {
        ('Pending', 'Pending'),
        ('Payment', 'Payment'),
        ('Waiting', 'Waiting'),
        ('Working', 'Working'),
        ('Complete', 'Complete'),
        ('Delivery', 'Delivery'),
        ('Cancel', 'Cancel'),
    }
    status = forms.CharField(max_length=20, label='Status', widget=forms.Select(
        attrs={'class': 'form-control'}, choices=STATUS
    ))


# class Payment_Form(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = '__all__'
#         widgets = {
#             'user': forms.Select(attrs={
#                 'class': 'form-control',
#             }),
#             'order_ID': forms.Select(attrs={
#                 'class': 'form-control'
#             }),
#             'payment_type': forms.Select(attrs={
#                 'class': 'form-control'
#             }),
#             'payment_method': forms.Select(attrs={
#                 'class': 'form-control'
#             }),
#             'bank': forms.TextInput(attrs={
#                 'class': 'form-control',
#             }),
#             'total_amount': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'account_holder_name': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'account_holder_email': forms.EmailInput(attrs={
#                 'class': 'form-control'
#             }),
#             'account_phone_number': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'transaction_id': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'account_number': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'account_info': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'transaction_receipt': forms.FileInput(attrs={
#                 'class': 'form-control'
#             }),
#         }


class Order_Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['total_price']
        widgets = {
            'product_title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Product Title'
            }),
            'product_price': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Product Price'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
