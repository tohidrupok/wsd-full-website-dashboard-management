from django.contrib import admin
from.models import *


@admin.register(MobileWallet)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','name','icon','qr_code','account_details','active']

@admin.register(OfflineBank)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','country_name','payment_person','payment_person_id','check_number','check_security_code','check_account','status',]

