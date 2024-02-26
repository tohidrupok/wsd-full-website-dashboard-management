from rest_framework import serializers
from .models import *

class Civil_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order
        fields = '__all__'


class Civil_Order_Work_DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_Work_Document
        fields = '__all__'


class Civil_OrderAdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_Admin_Note
        fields = '__all__'


class Civil_Order_Update_BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_Update_Box
        fields = '__all__'


class Civil_Order_User_Information_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_User_Information
        fields = '__all__'

class Civil_Order_Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_Product
        fields = '__all__'







# ==================================================
# Civil Order Payment Section Start
# ==================================================

class CivilPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Payment
        fields = '__all__'

class CivilBankPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_BankPayment
        fields = '__all__'

class CivilMobilePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_MobilePayment
        fields = '__all__'

class CivilOfflinePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_OfflinePayment
        fields = '__all__'

# ==================================================
# Civil Order Payment Section End
# ==================================================


# ==================================================
# Civil Order Refund serializers Section Start
# ==================================================
class CivilRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Refund
        fields = '__all__'

class CivilBankRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Bank_Refund
        fields = '__all__'

class CivilMobileRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Mobile_Refund
        fields = '__all__'
# ==================================================
# Civil Order Refund serializers Section End
# ==================================================


