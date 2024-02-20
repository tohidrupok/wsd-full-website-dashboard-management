from django.contrib import admin
from .models import *


@admin.register(WebsiteLogo)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','description','image']

@admin.register(WebsiteBanner)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','header_text','tag_text','image_and_video']

@admin.register(CardHomepageThreeOne,CardHomepageThreeTwo,CardHomepageThree)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','icon','title','tag_text','description']



@admin.register(CardHomepageTwo,CardHomepageFour)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','icon','title','tag_text','description']



@admin.register(CardTemplate)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','tag','price','url']


@admin.register(BlogCard)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','tag','description']

@admin.register(TimeData)
class apiAdmin(admin.ModelAdmin):
    list_display = ['id','year','month','day','hour','second']



admin.site.register(Homepage_Segment)
admin.site.register(Support_Company_Logo)
admin.site.register(Office_Address_1)
admin.site.register(Office_Address_2)
admin.site.register(Payment_Logo)
admin.site.register(Social_Media)
admin.site.register(Global_Location)
admin.site.register(Contact_Us)
admin.site.register(Subscribtions)
admin.site.register(Footer_Section_1)
admin.site.register(Footer_Section_1_Topics)
admin.site.register(Footer_Section_2)
admin.site.register(Footer_Section_2_Topics)
admin.site.register(Footer_Section_3)
admin.site.register(Footer_Section_3_Topics)
admin.site.register(Technology)
admin.site.register(Technology_Icon)
admin.site.register(Our_Services)
admin.site.register(Notice_Board)
admin.site.register(Order_Card)
admin.site.register(Security_Page)
admin.site.register(Company_Member)

