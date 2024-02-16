from django import forms
from .models import Order

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
