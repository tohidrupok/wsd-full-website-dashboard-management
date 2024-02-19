from rest_framework import serializers
from .models import Messages, Topic
from account.models import Custom_User

class MessageTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=Custom_User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=Custom_User.objects.all())

    class Meta:
        model = Messages
        fields = ['topic', 'sender', 'receiver', 'content', 'time']

