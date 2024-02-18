from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class Order_Work_DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Work_Document
        fields = '__all__'


class OrderAdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAdminNote
        fields = '__all__'


class Order_Update_BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Update_Box
        fields = '__all__'



