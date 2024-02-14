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


