from rest_framework import serializers
from .models import *

class Sound_Serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username')
    entry_sound = serializers.StringRelatedField(source='entry_sound.ringtone.url')
    live_chat_talk_sound = serializers.StringRelatedField(source='live_chat_talk_sound.ringtone.url')
    live_chat_turned_off_sound = serializers.StringRelatedField(source='live_chat_turned_off_sound.ringtone.url')
    live_chat_notification_sound = serializers.StringRelatedField(source='live_chat_notification_sound.ringtone.url')
    live_call_ringtone = serializers.StringRelatedField(source='live_call_ringtone.ringtone.url')
    user_cannot_call_admin_sound = serializers.StringRelatedField(source='user_cannot_call_admin_sound.ringtone.url')
    order_chat_notification_tone = serializers.StringRelatedField(source='order_chat_notification_tone.ringtone.url')
    order_call_ringtone = serializers.StringRelatedField(source='order_call_ringtone.ringtone.url')
    admin_chat_notification_sound = serializers.StringRelatedField(source='admin_chat_notification_sound.ringtone.url')
    admin_call_ringtone = serializers.StringRelatedField(source='admin_call_ringtone.ringtone.url')
    class Meta:
        model = Sound
        fields = '__all__'


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





