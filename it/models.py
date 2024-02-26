from django.db import models
from user.models import Website_User
from django.utils import timezone
from it_dashboard.sound_bank_models import IT_Bank, IT_MobileWallet, IT_OfflineCheck

class IT_Order(models.Model):
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
    
    user = models.ForeignKey(Website_User, on_delete=models.CASCADE, related_name='it_order')
    project_name = models.CharField(max_length=300)
    project_file = models.FileField(upload_to='it/order/project-file/', blank=True, null=True)
    related_file = models.FileField(upload_to='it/order/related-file/', blank=True, null=True)
    
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
        
        super(IT_Order, self).save(*args, **kwargs)

    class Meta:
        ordering = ['updated_date', 'created_date', 'delivery_date']
    
    def __str__(self) -> str:
        return f'{self.user.full_name} - {self.project_name}'
  

class IT_Order_Work_Document(models.Model):
    order = models.ForeignKey(IT_Order, on_delete=models.CASCADE, related_name='it_order_work_document')
    text_box = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='it/order/work-update/', blank=True, null=True)
    files = models.FileField(upload_to='it/order/work-update/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.order} {self.text_box}'


class IT_Order_Admin_Note(models.Model):
    order = models.ForeignKey(IT_Order, on_delete=models.CASCADE, related_name='it_order_note')
    text_box = models.TextField(blank=True, null=True)
    file_or_image = models.FileField(upload_to='it/order/note-file/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.order} | {self.text_box}'


class IT_Order_Update_Box(models.Model):
    order = models.OneToOneField(IT_Order, on_delete=models.CASCADE, related_name='it_order_update')
    content = models.TextField(blank=True, null=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"Order: {self.order}"

    class Meta:
        ordering = ('timestamp',)




class IT_Order_User_Information(models.Model):
    order = models.OneToOneField(IT_Order, on_delete=models.CASCADE, related_name='it_order_user_information')
    name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    educational_qualifications = models.TextField(blank=True, null=True)
    professional_details = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    work_experience = models.IntegerField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)

    profile_id = models.CharField(max_length=50, blank=True, null=True)
    application_date = models.DateField(auto_now_add=True)
    user_photo = models.ImageField(upload_to='it/order/user/', blank=True, null=True)
    user_signature = models.ImageField(upload_to='it/order/user/signature/', blank=True, null=True)
    company_signature = models.ImageField(upload_to='it/order/company/signature/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.order.user.full_name
        self.email_address = self.order.user.email
        self.gender = self.order.user.gender
        self.nationality = self.order.user.country
        self.profile_id = self.order.user
        super(IT_Order_User_Information, self).save(*args, **kwargs)


class IT_Order_Product(models.Model):
    order_profile_information = models.ForeignKey(IT_Order_User_Information, on_delete=models.CASCADE, related_name='it_order_product')

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name




# ==================================================
# IT Order Payment Models Section Start
# ==================================================
class IT_Payment(models.Model):
    order = models.ForeignKey(IT_Order, on_delete=models.CASCADE, related_name='it_order_payment')
    
    currency = models.CharField(max_length=3, choices=(('USD', 'USD'), ('BDT', 'BDT')), default='USD')
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=(('Online', 'Online'), ('Offline', 'Offline')))
    payment_method = models.CharField(max_length=10, choices=(('bank', 'Bank'), ('mobile', 'Mobile')))
    
    bank = models.ForeignKey(IT_Bank, on_delete=models.DO_NOTHING, related_name='it_bank')
    mobile_wallet = models.ForeignKey(IT_MobileWallet, on_delete=models.DO_NOTHING, related_name='it_mobile_wallet')
    
    status = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.order.project_name} - {self.pk}'


class IT_BankPayment(models.Model):
    payment = models.OneToOneField(IT_Payment, on_delete=models.CASCADE, related_name='bank_payment')
    
    account_holder_name = models.CharField(max_length=100)
    account_holder_email = models.EmailField()
    account_holder_phone = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=100, blank=False)
    account_number = models.CharField(max_length=50)
    account_info = models.TextField( blank=True)
    transaction_id = models.CharField(max_length=100,unique=True)
    transaction_receipt = models.ImageField(upload_to='it/image/transaction_receipts/')
    additional_info = models.TextField(blank=True)
    agree = models.BooleanField()
    
    def __str__(self) -> str:
        return f'{self.payment.order.project_name} - {self.pk}'

class IT_MobilePayment(models.Model):
    payment = models.OneToOneField(IT_Payment, on_delete=models.CASCADE, related_name='mobile_payment')
    
    account_holder_name = models.CharField(max_length=100)
    account_holder_email = models.EmailField()
    account_holder_phone = models.CharField(max_length=15)
    mobile_wallet_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    account_info = models.TextField()
    transaction_id = models.CharField(max_length=100,unique=True)
    transaction_receipt = models.ImageField(upload_to='it/image/transaction_receipts/')
    agree = models.BooleanField()
    
    def __str__(self) -> str:
        return f'{self.payment.order.project_name} - {self.pk}'

class IT_OfflinePayment(models.Model):
    payment = models.OneToOneField(IT_Payment, on_delete=models.CASCADE, related_name='offline_payment')
    
    country_name = models.CharField(max_length=100)
    receipt_person_name = models.CharField(max_length=100)
    receipt_person_id = models.CharField(max_length=100)
    
    check_holder_name = models.CharField(max_length=100)
    check_holder_gmail = models.EmailField()
    check_holder_phone_number = models.CharField(max_length=14)
    check_number = models.CharField(max_length=100)
    check_security_code = models.CharField(max_length=100)
    check_receipt = models.FileField(upload_to='it/image/check_receipt/')
    
    is_varified = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs) -> None:
        it_offline_payment_check = IT_OfflineCheck.objects.filter(
            payment_receipt_person_id=self.receipt_person_id,
            check_holder_phone_number = self.check_holder_phone_number,
            check_number = self.check_number,
            check_security_code = self.check_security_code,
        ).exists()
        if it_offline_payment_check:
            self.is_varified = True
        else:
            self.is_varified = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.check_holder_name} - {self.check_number} - {self.receipt_person_name} - {self.payment.pk}"

# ==================================================
# IT Order Payment Models Section End
# ==================================================



# ==================================================
# IT Order Refund Models Section Start
# ==================================================
class IT_Refund(models.Model):
    order = models.ForeignKey(IT_Order, on_delete=models.DO_NOTHING, blank=True, null=True)
    payment = models.OneToOneField(IT_Payment, on_delete=models.DO_NOTHING, blank=True, null=True)
    refund_method = models.CharField(max_length=50, choices=(('bank', 'Bank'), ('mobile', 'Mobile')), blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    refund_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, choices=(('Pending', 'Pending'), ('Processing', 'Processing'), ('Complete', 'Complete'), ('Cancel', 'Cancel')), default='Pending')
    
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    preferred_contact_method = models.CharField(max_length=20, blank=True, null=True)
    
    reason_for_refund = models.TextField()
    proof_of_payment = models.FileField(upload_to='it/image/refund_proofs/')
    additional_notes = models.TextField(blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)
    feedback_or_suggestions = models.TextField(blank=True, null=True)
    documentation_or_evidence = models.FileField(upload_to='it/image/refund_documents/', blank=True, null=True)
    specific_issue_details = models.TextField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.order.pk} | {self.payment.pk} | {self.name} | {self.email}'
    
    def save(self, *args, **kwargs):
        if self.payment.payment_type == 'Online':
            self.refund_method = self.payment.payment_method
        self.currency = self.payment.currency
        self.refund_amount = self.payment.payment_amount
        super(IT_Refund, self).save(*args, **kwargs)


class IT_Bank_Refund(models.Model):
    refund = models.OneToOneField(IT_Refund, on_delete=models.CASCADE)
    
    recipient_bank_name = models.CharField(max_length=100, blank=True, null=True)
    recipient_bank_account_name = models.CharField(max_length=100, blank=True, null=True)
    recipient_bank_account_number = models.CharField(max_length=100, blank=True, null=True)
    recipient_bank_routing_name = models.CharField(max_length=100, blank=True, null=True)
    iban_or_swift_code = models.CharField(max_length=100, blank=True, null=True)
    account_info = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.refund.pk} | {self.recipient_bank_name} | {self.recipient_bank_account_name} | {self.recipient_bank_account_number}'

class IT_Mobile_Refund(models.Model):
    refund = models.OneToOneField(IT_Refund, on_delete=models.CASCADE)
    
    recipient_mobile_wallet_name = models.CharField(max_length=100, blank=True, null=True)
    recipient_wallet_account_name = models.CharField(max_length=100, blank=True, null=True)
    recipient_wallet_account_number = models.CharField(max_length=100, blank=True, null=True)
    account_info = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.refund.pk} | {self.recipient_mobile_wallet_name} | {self.recipient_wallet_account_name} | {self.recipient_wallet_account_number}'

# ==================================================
# IT Order Refund Models Section End
# ==================================================


