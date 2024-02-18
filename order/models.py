from django.db import models
from account.models import Custom_User

class Order(models.Model):
    PIORITY = (
        ('Normal', 'Normal'),
        ('Medium', 'Medium'),
        ('Emergency', 'Emergency'),
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Payment', 'Payment'),
        ('Waiting', 'Waiting'),
        ('Working', 'Working'),
        ('Complited', 'Complited'),
        ('Cancel', 'Cancel'),
    )
    CURRENCY = (
        ('USD', 'USD'),
        ('BDT', 'BDT'),
        ('INR', 'INR'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        ('CAD', 'CAD'),
    )
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='order')
    project_name = models.CharField(max_length=300)
    project_file = models.FileField(upload_to='static/project-file/', blank=True, null=True)
    related_file = models.FileField(upload_to='static/project-file/', blank=True, null=True)
    
    status = models.CharField(max_length=40, choices=STATUS)
    piority = models.CharField(max_length=40, choices=PIORITY)
    currency = models.CharField(max_length=20, blank=True, null=True, choices=CURRENCY)
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_online_deposite = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_offline_deposite = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount_remain = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    profit_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    delivery_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.total_amount:
            self.total_amount = 0
        if not self.total_online_deposite:
            self.total_online_deposite = 0
        if not self.total_offline_deposite:
            self.total_offline_deposite = 0
        if not self.profit_amount:
            self.profit_amount = 0
        
        self.total_amount_paid = self.total_offline_deposite + self.total_online_deposite
        self.total_amount_remain = self.total_amount - self.total_amount_paid
        
        super(Order, self).save(*args, **kwargs)

    
    class Meta:
        ordering = ['updated_date', 'created_date', 'delivery_date']
    
    def __str__(self) -> str:
        return f'{self.user.name} - {self.project_name}'
    
    


class Order_Work_Document(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_work_document')
    text_box = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/work-update/', blank=True, null=True)
    files = models.FileField(upload_to='static/work-update/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.order} {self.text_box}'


class OrderAdminNote(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_note')
    text_box = models.TextField(blank=True, null=True)
    file_or_image = models.FileField(upload_to='static/note-file/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.order} | {self.text_box}'


class Order_Update_Box(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_update')
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/message_images/', blank=True, null=True)
    
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: {self.order}"

    class Meta:
        ordering = ('timestamp',)


    
    
    




