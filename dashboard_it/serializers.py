from rest_framework import serializers
from .models import *


class WebsiteLogoSerializerit(serializers.ModelSerializer):
    class Meta:
        model = WebsiteLogo
        fields = '__all__'

class WebsiteBannerSerializerit(serializers.ModelSerializer):
    class Meta:
        model = WebsiteBanner
        fields = '__all__'



class CardSerializerTwoOneit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageTwoOne
        fields = '__all__'


class CardSerializerTwoit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageTwo
        fields = '__all__'



class CardSerializerThreeOneit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageThreeOne
        fields = '__all__'


class CardSerializerThreeTwoit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageThreeTwo
        fields = '__all__'


class CardSerializerThreeit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageThree
        fields = '__all__'



class CardSerializerFourOneit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageFourOne
        fields = '__all__'


class CardSerializerFourTwoit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageFourTwo
        fields = '__all__'


class CardSerializerFourThreeit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageFourThree
        fields = '__all__'


class CardSerializerFourit(serializers.ModelSerializer):
    class Meta:
        model = CardHomepageFour
        fields = '__all__'



class CardTemplateSerializerit(serializers.ModelSerializer):
    class Meta:
        model = CardTemplate
        fields = '__all__'

class BlogCardSerializerit(serializers.ModelSerializer):
    class Meta:
        model = BlogCard
        fields = '__all__'

class TimeDataSerializerit(serializers.ModelSerializer):
    class Meta:
        model = TimeData
        fields = '__all__'



class HomepageSegmentSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Homepage_Segment
        fields = '__all__'

class SupportCompanyLogoSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Support_Company_Logo
        fields = '__all__'

class OfficeAddress1Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Office_Address_1
        fields = '__all__'

class OfficeAddress2Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Office_Address_2
        fields = '__all__'

class PaymentLogoSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Payment_Logo
        fields = '__all__'

class SocialMediaSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Social_Media
        fields = '__all__'

class GlobalLocationSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Global_Location
        fields = '__all__'

class ContactUsSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = '__all__'

class SubscribtionsSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Subscribtions
        fields = '__all__'



class Footer_Section_1_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Footer_Section_1
        fields = '__all__'

class Footer_Section_1_Topics_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Footer_Section_1_Topics
        fields = '__all__'


class Footer_Section_2_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Footer_Section_2
        fields = '__all__'

class Footer_Section_2_Topics_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Footer_Section_2_Topics
        fields = '__all__'


class Footer_Section_3_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Footer_Section_3
        fields = '__all__'

class Footer_Section_3_Topics_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Footer_Section_3_Topics
        fields = '__all__'



class Technology_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class Technology_Icon_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Technology_Icon
        fields = '__all__'


class Our_Services_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Our_Services
        fields = '__all__'

class Notice_Board_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Notice_Board
        fields = '__all__'

class Security_Page_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Security_Page
        fields = '__all__'

class Order_Card_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Order_Card
        fields = '__all__'

class Company_Member_Serializerit(serializers.ModelSerializer):
    class Meta:
        model = Company_Member
        fields = '__all__'



