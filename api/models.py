from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='image/bank_icons/')
    qr_code = models.ImageField(upload_to='image/bank_qr_codes/')
    account_details = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.icon}-{self.qr_code} {self.account_details}:{self.active}"

class MobileWallet(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='image/mobile_wallet_icons/')
    qr_code = models.ImageField(upload_to='image/mobile_wallet_qr_codes/')
    account_details = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.icon}-{self.qr_code} {self.account_details}:{self.active}"


class OfflineBank(models.Model):
    country_name = models.CharField(max_length=100)
    payment_person = models.CharField(max_length=100)
    payment_person_id = models.CharField(max_length=100)
    check_number = models.CharField(max_length=100)
    check_security_code = models.CharField(max_length=100)
    currency_iso = models.CharField(max_length=3)
    check_account = models.CharField(max_length=100)
    status = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.country_name}-{self.payment_person}-{self.payment_person_id} {self.check_number}:{self.check_security_code}-{self.currency_iso} {self.check_account}:{self.status}"


