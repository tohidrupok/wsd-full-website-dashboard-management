from rest_framework import serializers
from .models import *

class EntrySound_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EntrySound
        fields = '__all__'


class Live_Chat_Talk_Sound_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Chat_Talk_Sound
        fields = '__all__'

class Live_Chat_Turned_Off_Sound_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Chat_Turned_Off_Sound
        fields = '__all__'

class Live_Chat_Notification_Sound_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Chat_Notification_Sound
        fields = '__all__'


class Live_Call_Ringtone_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Call_Ringtone
        fields = '__all__'

class User_Cannot_Call_Admin_Sound_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Cannot_Call_Admin_Sound
        fields = '__all__'


class Order_Chat_Notification_Tone_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Chat_Notification_Tone
        fields = '__all__'


class Order_Call_Ringtone_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Call_Ringtone
        fields = '__all__'


class Admin_Chat_Notification_Sound_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Chat_Notification_Sound
        fields = '__all__'

class Admin_Call_Ringtone_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Call_Ringtone
        fields = '__all__'


class Sound_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = '__all__'


