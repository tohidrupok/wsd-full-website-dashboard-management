from django.db import models

class User_Sound(models.Model):
    website_entry_sound = models.FileField(upload_to='sound/entry_sound/', blank=True, null=True)
    live_chat_talk_sound = models.FileField(upload_to='sound/live_chat_talk_sound/', blank=True, null=True)
    live_chat_turned_off_sound = models.FileField(upload_to='sound/live_chat_turned_off_sound/', blank=True, null=True)
    user_live_chat_notification_sound = models.FileField(upload_to='sound/user_live_chat_notification_sound/', blank=True, null=True)
    user_live_call_ringtone = models.FileField(upload_to='sound/user_live_call_ringtone/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'User Sound {self.pk}'


class User_Order_Sound(models.Model):
    order_chat_notification_tone = models.FileField(upload_to='sound/order_chat_notification_tone/', blank=True, null=True)
    order_call_ringtone = models.FileField(upload_to='sound/order_call_ringtone/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'User Order Sound {self.pk}'


class Live_Chat_Admin_Sound(models.Model):
    admin_live_chat_notification_sound = models.FileField(upload_to='sound/admin_live_chat_notification_sound/', blank=True, null=True)
    admin_live_call_ringtone = models.FileField(upload_to='sound/admin_live_call_ringtone/', blank=True, null=True)
    user_cannot_call_admin_sound = models.FileField(upload_to='sound/user_cannot_call_admin_sound/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Admin Live Chat Sound {self.pk}'






