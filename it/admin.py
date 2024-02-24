from django.contrib import admin
from .models import *

@admin.register(IT_Order)
class IT_OrderAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'status', 'piority', 'currency', 'total_amount', 'total_amount_paid', 'total_amount_remain', 'delivery_date')
    list_filter = ('status', 'piority', 'currency', 'delivery_date', 'created_date', 'updated_date')
    search_fields = ('user__name', 'project_name', 'status', 'piority', 'currency')


class IT_Order_Work_DocumentAdmin(admin.ModelAdmin):
    list_display = ('order', 'text_box', 'image', 'files', 'updated_date')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('order__user__name', 'text_box')

admin.site.register(IT_Order_Work_Document, IT_Order_Work_DocumentAdmin)


class IT_OrderAdminNoteAdmin(admin.ModelAdmin):
    list_display = ('order', 'text_box', 'file_or_image', 'updated_date')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('order__user__name', 'text_box')

admin.site.register(IT_Order_Admin_Note, IT_OrderAdminNoteAdmin)


class IT_Order_Update_BoxAdmin(admin.ModelAdmin):
    list_display = ('order', 'content', 'time', 'seen', 'timestamp')
    list_filter = ('seen', 'timestamp')
    search_fields = ('order__user__name', 'content')

admin.site.register(IT_Order_Update_Box, IT_Order_Update_BoxAdmin)


class IT_Order_User_InformationAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'date_of_birth', 'gender', 'nationality', 'phone_number', 'email_address')
    list_filter = ('gender', 'nationality', 'occupation', 'application_date')
    search_fields = ('order__user__name', 'name', 'email_address', 'occupation')

admin.site.register(IT_Order_User_Information, IT_Order_User_InformationAdmin)


class IT_Order_ProductAdmin(admin.ModelAdmin):
    list_display = ('order_profile_information', 'name', 'category', 'brand', 'color', 'size')
    list_filter = ('category', 'brand', 'color', 'size')
    search_fields = ('order_profile_information__name', 'name', 'category', 'brand', 'color', 'size')

admin.site.register(IT_Order_Product, IT_Order_ProductAdmin)

