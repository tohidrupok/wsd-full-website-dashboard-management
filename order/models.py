from django.db import models
from admin_account.models import Custom_User



class Order(models.Model):
    STATUS = {
        ('Pending', 'Pending'),
        ('Payment', 'Payment'),
        ('Waiting', 'Waiting'),
        ('Working', 'Working'),
        ('Complete', 'Complete'),
        ('Delivery', 'Delivery'),
        ('Cancel', 'Cancel'),
    }
    product_title = models.CharField(max_length=500)
    product_price = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS, max_length=20, default='Pending')
    total_price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    
    order_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.total_price = self.product_price * self.quantity
        super(Order, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.product_title} x {self.quantity}'


# class Payment_Type(models.Model):
#     title = models.CharField()


class Payment(models.Model):
    PAYMENT_TYPE = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    )
    PAYMENT_METHOD = (
        ('Bank', 'Bank'),
        ('Moblie Walet', 'Moblie Walet'),
    )
    
    user = models.ForeignKey(Custom_User, on_delete=models.DO_NOTHING, related_name='user_payment', blank=True, null=True) #foreignkey with user or customer
    bank = models.CharField(max_length=50, blank=True, null=True) #foreignkey with user or customer
    
    order_ID = models.OneToOneField(Order, on_delete=models.DO_NOTHING, related_name='order_payment')
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    
    account_holder_name = models.CharField(max_length=100)
    account_holder_email = models.EmailField(max_length=100)
    account_phone_number = models.CharField(max_length=14)
    transaction_id = models.CharField(max_length=50, unique=True)
    account_number = models.CharField(max_length=100)
    account_info = models.CharField(max_length=100)
    transaction_receipt = models.FileField(upload_to='payment/transaction/', blank=True, null=True)
    
    



