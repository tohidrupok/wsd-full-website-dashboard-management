from django.db import models
from account.models import Custom_User
from django.utils import timezone

class Topic(models.Model):
    admin_user = models.ManyToManyField(Custom_User, related_name='chat_topic')
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class Messages(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sender = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name="receiver", blank=True, null=True)
    content = models.TextField()
    
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"Topic: {self.topic} User: {self.sender}"

    class Meta:
        ordering = ('timestamp',)

