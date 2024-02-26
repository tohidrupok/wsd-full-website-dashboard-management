from django.db import models

# ==================================================
# Payment Method Models For Whole Website Start
# ==================================================
#Bank Models-------------
class Civil_Bank(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='civil/image/bank_icons/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='civil/image/bank_qr_codes/', blank=True, null=True)
    account_details = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.icon}-{self.qr_code} {self.account_details}:{self.active}"

#Mobile Wallet Models-------------
class Civil_MobileWallet(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='civil/image/mobile_wallet_icons/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='civil/image/mobile_wallet_qr_codes/', blank=True, null=True)
    account_details = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.icon}-{self.qr_code} {self.account_details}:{self.active}"


# Offline Models-------------
class Civil_OfflineCheck(models.Model):
    country_name = models.CharField(max_length=100)
    payment_receipt_person_name = models.CharField(max_length=100)
    payment_receipt_person_id = models.CharField(max_length=100)
    
    check_holder_name = models.CharField(max_length=100)
    check_holder_gmail = models.EmailField()
    check_holder_phone_number = models.CharField(max_length=14)
    check_number = models.CharField(max_length=100)
    check_security_code = models.CharField(max_length=100)
    currency_iso = models.CharField(max_length=3)
    check_amount = models.CharField(max_length=100)
    
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.country_name}-{self.check_holder_name}-{self.check_number} {self.check_amount} : {self.payment_receipt_person_name}-{self.payment_receipt_person_id} {self.country_name}"

# ==================================================
# Payment Method Models For Whole Website End
# ==================================================



# ==================================================
# Website Sound System Models For Whole Website Start
# ==================================================
class Civil_Live_Chat_Admin_Sound(models.Model):
    admin_live_chat_notification_sound = models.FileField(upload_to='civil/sound/admin_live_chat_notification_sound/', blank=True, null=True)
    admin_live_call_ringtone = models.FileField(upload_to='civil/sound/admin_live_call_ringtone/', blank=True, null=True)
    user_cannot_call_admin_sound = models.FileField(upload_to='civil/sound/user_cannot_call_admin_sound/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Admin Live Chat Sound {self.pk}'

class Civil_User_Sound(models.Model):
    website_entry_sound = models.FileField(upload_to='civil/sound/entry_sound/', blank=True, null=True)
    live_chat_talk_sound = models.FileField(upload_to='civil/sound/live_chat_talk_sound/', blank=True, null=True)
    live_chat_turned_off_sound = models.FileField(upload_to='civil/sound/live_chat_turned_off_sound/', blank=True, null=True)
    user_live_chat_notification_sound = models.FileField(upload_to='civil/sound/user_live_chat_notification_sound/', blank=True, null=True)
    user_live_call_ringtone = models.FileField(upload_to='civil/sound/user_live_call_ringtone/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'User Sound {self.pk}'


class Civil_User_Order_Sound(models.Model):
    order_chat_notification_tone = models.FileField(upload_to='civil/sound/order_chat_notification_tone/', blank=True, null=True)
    order_call_ringtone = models.FileField(upload_to='civil/sound/order_call_ringtone/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'User Order Sound {self.pk}'
# ==================================================
# Website Sound System Models For Whole Website End
# ==================================================


