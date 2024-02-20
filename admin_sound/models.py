from django.db import models

class Live_Chat_Admin_Sound(models.Model):
    admin_live_chat_notification_sound = models.FileField(upload_to='sound/admin_live_chat_notification_sound/', blank=True, null=True)
    admin_live_call_ringtone = models.FileField(upload_to='sound/admin_live_call_ringtone/', blank=True, null=True)
    user_cannot_call_admin_sound = models.FileField(upload_to='sound/user_cannot_call_admin_sound/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Admin Live Chat Sound {self.pk}'


