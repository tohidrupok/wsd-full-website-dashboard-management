from rest_framework import serializers
from .models import *

class LiveChatAdminSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Chat_Admin_Sound
        fields = '__all__'


