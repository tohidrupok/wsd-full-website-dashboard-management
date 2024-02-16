from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Custom_User

@admin.register(Custom_User)
class Custom_User_Admin(admin.ModelAdmin):
    list_display = ['email', 'username', 'user_type', 'update_date']
    list_filter = ['user_type']
    search_fields = ['email', 'username', 'user_type']

    

admin.site.register(Permission)
