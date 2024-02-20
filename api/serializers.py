from rest_framework import serializers
from .models import *

class BankSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class MobileWalletSerializerit(serializers.ModelSerializer):
    class Meta:
        model = MobileWallet
        fields = '__all__'


class OfflineBankSerializerit(serializers.ModelSerializer):
    class Meta:
        model = OfflineBank
        fields = '__all__'


