from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

"""====== Start_Logo_Api_View ======"""

class WebsiteLogoCreateit(generics.ListCreateAPIView):
    queryset = WebsiteLogo.objects.all()
    serializer_class = WebsiteLogoSerializerit

class WebsiteLogoUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = WebsiteLogo.objects.all()
    serializer_class = WebsiteLogoSerializerit

"""====== End_Logo_Api_View ======"""



"""====== Start_Banner_Api_View ======"""
class WebsiteBannerCreateit(generics.ListCreateAPIView):
    queryset = WebsiteBanner.objects.all()
    serializer_class = WebsiteBannerSerializerit

class WebsiteBannerUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = WebsiteBanner.objects.all()
    serializer_class = WebsiteBannerSerializerit
"""====== End_Banner_Api_View ======"""







"""====== Start_Card_Api_View_Two ======"""

class CardCreateHomepageTwoOneit(generics.ListCreateAPIView):
    queryset = CardHomepageTwoOne.objects.all()
    serializer_class = CardSerializerTwoOneit

class CardUpdateHomepageTwoOneit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageTwoOne.objects.all()
    serializer_class = CardSerializerTwoOneit



class CardCreateHomepageTwoit(generics.ListCreateAPIView):
    queryset = CardHomepageTwo.objects.all()
    serializer_class = CardSerializerTwoit

class CardUpdateHomepageTwoit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageTwo.objects.all()
    serializer_class = CardSerializerTwoit


"""====== End_Banner_Api_View_Two ======"""







"""====== Start_Card_Api_View_Three ======"""

class CardCreateHomepageThreeOneit(generics.ListCreateAPIView):
    queryset = CardHomepageThreeOne.objects.all()
    serializer_class = CardSerializerThreeOneit

class CardUpdateHomepageThreeOneit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageThreeOne.objects.all()
    serializer_class = CardSerializerThreeOneit



class CardCreateHomepageThreeTwoit(generics.ListCreateAPIView):
    queryset = CardHomepageThreeTwo.objects.all()
    serializer_class = CardSerializerThreeTwoit

class CardUpdateHomepageThreeTwoit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageThreeTwo.objects.all()
    serializer_class = CardSerializerThreeTwoit



class CardCreateHomepageThreeit(generics.ListCreateAPIView):
    queryset = CardHomepageThree.objects.all()
    serializer_class = CardSerializerThreeit

class CardUpdateHomepageThreeit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageThree.objects.all()
    serializer_class = CardSerializerThreeit
"""====== End_Banner_Api_View_Three ======"""







"""====== Start_Card_Api_View_Four ======"""


class CardCreateHomepageFourOneit(generics.ListCreateAPIView):
    queryset = CardHomepageFourOne.objects.all()
    serializer_class = CardSerializerFourOneit

class CardUpdateHomepageFourOneit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageFourOne.objects.all()
    serializer_class = CardSerializerFourOneit


class CardCreateHomepageFourTwoit(generics.ListCreateAPIView):
    queryset = CardHomepageFourTwo.objects.all()
    serializer_class = CardSerializerFourTwoit

class CardUpdateHomepageFourTwoit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageFourTwo.objects.all()
    serializer_class = CardSerializerFourTwoit



class CardCreateHomepageFourThreeit(generics.ListCreateAPIView):
    queryset = CardHomepageFourThree.objects.all()
    serializer_class = CardSerializerFourThreeit

class CardUpdateHomepageFourThreeit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageFourThree.objects.all()
    serializer_class = CardSerializerFourThreeit



class CardCreateHomepageFourit(generics.ListCreateAPIView):
    queryset = CardHomepageFour.objects.all()
    serializer_class = CardSerializerFourit

class CardUpdateHomepageFourit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardHomepageFour.objects.all()
    serializer_class = CardSerializerFourit
"""====== End_Banner_Api_View_Four ======"""









"""====== Start_Card_Template_Api_View ======"""
class CardTemplateCreateit(generics.ListCreateAPIView):
    queryset = CardTemplate.objects.all()
    serializer_class = CardTemplateSerializerit

class CardTemplateUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardTemplate.objects.all()
    serializer_class = CardTemplateSerializerit
"""====== End_Card_Template_Api_View ======"""



"""====== Start_blog_Card_Api_View ======"""
class BlogCardCreateit(generics.ListCreateAPIView):
    queryset = BlogCard.objects.all()
    serializer_class = BlogCardSerializerit

class BlogCardUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCard.objects.all()
    serializer_class = BlogCardSerializerit
"""====== End_blog_Card_Api_View ======"""




"""====== Start_Time_Api_View ======"""
class TimeDataCreateit(generics.ListCreateAPIView):
    queryset = TimeData.objects.all()
    serializer_class = TimeDataSerializerit

class TimeDataUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeData.objects.all()
    serializer_class = TimeDataSerializerit
"""====== End_blog_Card_Time_Api_View ======"""



# ===========================Start Homepage_Segment=================================
class Homepage_Segmentit(generics.ListCreateAPIView):
    queryset = Homepage_Segment.objects.all()
    serializer_class = HomepageSegmentSerializerit

class Homepage_SegmentUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homepage_Segment.objects.all()
    serializer_class = HomepageSegmentSerializerit
# ===========================End Homepage_Segment=================================


# ===========================Start Support_Company_Logo=================================
class Support_Company_Logoit(generics.ListCreateAPIView):
    queryset = Support_Company_Logo.objects.all()
    serializer_class = SupportCompanyLogoSerializerit

class Support_Company_LogoUpdateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Support_Company_Logo.objects.all()
    serializer_class = SupportCompanyLogoSerializerit
# ===========================End Support_Company_Logo=================================


# ===========================Start Office_Address_2=================================
class Office_Address_1_it(generics.ListCreateAPIView):
    queryset = Office_Address_1.objects.all()
    serializer_class = OfficeAddress1Serializerit

class Office_Address_1_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office_Address_1.objects.all()
    serializer_class = OfficeAddress1Serializerit


class Office_Address_2_it(generics.ListCreateAPIView):
    queryset = Office_Address_2.objects.all()
    serializer_class = OfficeAddress2Serializerit

class Office_Address_2_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office_Address_2.objects.all()
    serializer_class = OfficeAddress2Serializerit
# ===========================End Office_Address_2=================================




# ===========================Start Payment_Logo=================================
class Payment_Logo_it(generics.ListCreateAPIView):
    queryset = Payment_Logo.objects.all()
    serializer_class = PaymentLogoSerializerit

class Payment_Logo_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment_Logo.objects.all()
    serializer_class = PaymentLogoSerializerit
# ===========================End Payment_Logo=================================

# ===========================Start Social_Media=================================
class Social_Media_it(generics.ListCreateAPIView):
    queryset = Social_Media.objects.all()
    serializer_class = SocialMediaSerializerit

class Social_Media_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Social_Media.objects.all()
    serializer_class = SocialMediaSerializerit
# ===========================End Social_Media=================================

# ===========================Start Global_Location=================================
class Global_Location_it(generics.ListCreateAPIView):
    queryset = Global_Location.objects.all()
    serializer_class = GlobalLocationSerializerit

class Global_Location_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Global_Location.objects.all()
    serializer_class = GlobalLocationSerializerit
# ===========================End Global_Location=================================


# ===========================Start Contact_Us=================================
class Contact_Us_it(generics.ListCreateAPIView):
    queryset = Contact_Us.objects.all()
    serializer_class = ContactUsSerializerit

class Contact_Us_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact_Us.objects.all()
    serializer_class = ContactUsSerializerit
# ===========================End Contact_Us=================================

# ===========================Start Subscribtions=================================
class Subscribtions_it(generics.ListCreateAPIView):
    queryset = Subscribtions.objects.all()
    serializer_class = SubscribtionsSerializerit

class Subscribtions_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscribtions.objects.all()
    serializer_class = SubscribtionsSerializerit
# ===========================End Subscribtions=================================




# ===========================Start Footer_Section_1=================================
class Footer_Section_1_it(generics.ListCreateAPIView):
    queryset = Footer_Section_1.objects.all()
    serializer_class = Footer_Section_1_Serializerit

class Footer_Section_1_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer_Section_1.objects.all()
    serializer_class = Footer_Section_1_Serializerit

class Footer_Section_1_Topics_it(generics.ListCreateAPIView):
    queryset = Footer_Section_1_Topics.objects.all()
    serializer_class = Footer_Section_1_Topics_Serializerit

class Footer_Section_1_Topics_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer_Section_1_Topics.objects.all()
    serializer_class = Footer_Section_1_Topics_Serializerit
# ===========================End Footer_Section_1=================================


# ===========================Start Footer_Section_2=================================
class Footer_Section_2_it(generics.ListCreateAPIView):
    queryset = Footer_Section_2.objects.all()
    serializer_class = Footer_Section_2_Serializerit

class Footer_Section_2_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer_Section_2.objects.all()
    serializer_class = Footer_Section_2_Serializerit

class Footer_Section_2_Topics_it(generics.ListCreateAPIView):
    queryset = Footer_Section_2_Topics.objects.all()
    serializer_class = Footer_Section_2_Topics_Serializerit

class Footer_Section_2_Topics_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer_Section_2_Topics.objects.all()
    serializer_class = Footer_Section_2_Topics_Serializerit
# ===========================End Footer_Section_2=================================



# ===========================Start Footer_Section_3=================================
class Footer_Section_3_it(generics.ListCreateAPIView):
    queryset = Footer_Section_3.objects.all()
    serializer_class = Footer_Section_3_Serializerit

class Footer_Section_3_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer_Section_3.objects.all()
    serializer_class = Footer_Section_3_Serializerit

class Footer_Section_3_Topics_it(generics.ListCreateAPIView):
    queryset = Footer_Section_3_Topics.objects.all()
    serializer_class = Footer_Section_3_Topics_Serializerit

class Footer_Section_3_Topics_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer_Section_3_Topics.objects.all()
    serializer_class = Footer_Section_3_Topics_Serializerit
# ===========================End Footer_Section_3=================================



# ===========================Start Technology=================================
class Technology_it(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = Technology_Serializerit

class Technology_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = Technology_Serializerit

class Technology_Icon_it(generics.ListCreateAPIView):
    queryset = Technology_Icon.objects.all()
    serializer_class = Technology_Icon_Serializerit

class Technology_Icon_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology_Icon.objects.all()
    serializer_class = Technology_Icon_Serializerit
# ===========================End Technology=================================




# ===========================Start Our_Services=================================
class Our_Services_it(generics.ListCreateAPIView):
    queryset = Our_Services.objects.all()
    serializer_class = Our_Services_Serializerit

class Our_Services_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Our_Services.objects.all()
    serializer_class = Our_Services_Serializerit
# ===========================End Our_Services=================================

# ===========================Start Notice_Board=================================
class Notice_Board_it(generics.ListCreateAPIView):
    queryset = Notice_Board.objects.all()
    serializer_class = Notice_Board_Serializerit

class Notice_Board_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice_Board.objects.all()
    serializer_class = Notice_Board_Serializerit
# ===========================End Notice_Board=================================

# ===========================Start Security_Page=================================
class Security_Page_it(generics.ListCreateAPIView):
    queryset = Security_Page.objects.all()
    serializer_class = Security_Page_Serializerit

class Security_Page_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Security_Page.objects.all()
    serializer_class = Security_Page_Serializerit
# ===========================End Security_Page=================================

# ===========================Start Order_Card=================================
class Order_Card_it(generics.ListCreateAPIView):
    queryset = Order_Card.objects.all()
    serializer_class = Order_Card_Serializerit

class Order_Card_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order_Card.objects.all()
    serializer_class = Order_Card_Serializerit
# ===========================End Order_Card=================================


# ===========================Start Company_Member=================================
class Company_Member_it(generics.ListCreateAPIView):
    queryset = Company_Member.objects.all()
    serializer_class = Company_Member_Serializerit

class Company_Member_Updateit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company_Member.objects.all()
    serializer_class = Company_Member_Serializerit
# ===========================End Company_Member=================================

