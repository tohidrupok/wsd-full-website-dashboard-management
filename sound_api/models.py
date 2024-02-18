from django.db import models
from account.models import Custom_User

class EntrySound(models.Model):
    ringtone = models.FileField(upload_to='static/sound/entry_sound/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name

class Live_Chat_Talk_Sound(models.Model):
    ringtone = models.FileField(upload_to='static/sound/live_chat_talk_sound/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name

class Live_Chat_Turned_Off_Sound(models.Model):
    ringtone = models.FileField(upload_to='static/sound/live_chat_turned_off_sound/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name


class Live_Chat_Notification_Sound(models.Model):
    ringtone = models.FileField(upload_to='static/sound/live_chat_notification_sound/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name


class Live_Call_Ringtone(models.Model):
    ringtone = models.FileField(upload_to='static/sound/live_call_ringtone/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name


class User_Cannot_Call_Admin_Sound(models.Model):
    ringtone = models.FileField(upload_to='static/sound/user_cannot_call_admin_sound/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name


class Order_Chat_Notification_Tone(models.Model):
    ringtone = models.FileField(upload_to='static/sound/order_chat_notification_tone/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name


class Order_Call_Ringtone(models.Model):
    ringtone = models.FileField(upload_to='static/sound/order_call_ringtone/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name


class Admin_Chat_Notification_Sound(models.Model):
    ringtone = models.FileField(upload_to='static/sound/admin_chat_notification_sound/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name


class Admin_Call_Ringtone(models.Model):
    ringtone = models.FileField(upload_to='static/sound/admin_call_ringtone/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.ringtone.name



class Sound(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, null=True, blank=True)
    
    entry_sound = models.ForeignKey(EntrySound, on_delete=models.DO_NOTHING, blank=True, null=True)
    live_chat_talk_sound = models.ForeignKey(Live_Chat_Talk_Sound, on_delete=models.DO_NOTHING, blank=True, null=True)
    live_chat_turned_off_sound = models.ForeignKey(Live_Chat_Turned_Off_Sound, on_delete=models.DO_NOTHING, blank=True, null=True)
    live_chat_notification_sound = models.ForeignKey(Live_Chat_Notification_Sound, on_delete=models.DO_NOTHING, blank=True, null=True)
    live_call_ringtone = models.ForeignKey(Live_Call_Ringtone, on_delete=models.DO_NOTHING, blank=True, null=True)
    user_cannot_call_admin_sound = models.ForeignKey(User_Cannot_Call_Admin_Sound, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    order_chat_notification_tone = models.ForeignKey(Order_Chat_Notification_Tone, on_delete=models.DO_NOTHING, blank=True, null=True)
    order_call_ringtone = models.ForeignKey(Order_Call_Ringtone, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    admin_chat_notification_sound = models.ForeignKey(Admin_Chat_Notification_Sound, on_delete=models.DO_NOTHING, blank=True, null=True)
    admin_call_ringtone = models.ForeignKey(Admin_Call_Ringtone, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"Sound settings for {self.user}"




