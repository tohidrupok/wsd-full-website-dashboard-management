from django.db import models
from account.models import Custom_User

class Topic(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class Messages(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sender = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='sender')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/message_images/', blank=True, null=True)
    
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Topic: {self.topic} User: {self.sender}"

    class Meta:
        ordering = ('timestamp',)
