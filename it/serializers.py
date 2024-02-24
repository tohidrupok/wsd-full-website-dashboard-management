from rest_framework import serializers
from .models import *

class IT_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order
        fields = '__all__'


class IT_Order_Work_DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_Work_Document
        fields = '__all__'


class IT_OrderAdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_Admin_Note
        fields = '__all__'


class IT_Order_Update_BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_Update_Box
        fields = '__all__'


class IT_Order_User_Information_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_User_Information
        fields = '__all__'

class IT_Order_Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_Product
        fields = '__all__'



# ==================================================
# IT Order Payment Serializers Section Start
# ==================================================
class ITPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Payment
        fields = '__all__'

class ITBankPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_BankPayment
        fields = '__all__'

class ITMobilePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_MobilePayment
        fields = '__all__'
# ==================================================
# IT Order Payment Serializers Section End
# ==================================================

