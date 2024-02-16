from rest_framework import serializers
from .models import Payment

class Payment_Serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username')
    class Meta:
        model = Payment
        fields = '__all__'
