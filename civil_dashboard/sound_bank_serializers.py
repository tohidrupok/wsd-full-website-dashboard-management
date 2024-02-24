from rest_framework import serializers
from .sound_bank_models import *


# ==================================================
# Payment Method Serializers For Whole Website Start
# ==================================================
class CivilBankSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Civil_Bank
        fields = '__all__'

class CivilMobileWalletSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Civil_MobileWallet
        fields = '__all__'

# ==================================================
# Payment Method Serializers For Whole Website End
# ==================================================



# ==================================================
# Website Sound System Serializers For Whole Website Start
# ==================================================
class Civil_LiveChatAdminSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Live_Chat_Admin_Sound
        fields = '__all__'

class Civil_UserSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_User_Sound
        fields = '__all__'

class Civil_UserOrderSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_User_Order_Sound
        fields = '__all__'
# ==================================================
# Website Sound System Serializers For Whole Website End
# ==================================================