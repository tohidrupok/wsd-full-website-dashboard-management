from rest_framework import serializers
from .models import Bank_Payment, Mobile_Banking_Payment

class Bank_Payment_Serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username')
    class Meta:
        model = Bank_Payment
        fields = '__all__'

class Mobile_Banking_Payment_Serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username')
    class Meta:
        model = Mobile_Banking_Payment
        fields = '__all__'




