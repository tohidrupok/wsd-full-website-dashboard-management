from rest_framework import serializers
from .models import *

class UserSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Sound
        fields = '__all__'

class UserOrderSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Order_Sound
        fields = '__all__'

class LiveChatAdminSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Chat_Admin_Sound
        fields = '__all__'




