from django.urls import path
from .views import *
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   #======= Start_logo_api_url =======
   path('it/logo/', WebsiteLogoCreateit.as_view(), name='logo_create'),
   path('it/logo/<int:pk>', WebsiteLogoUpdateit.as_view(), name='logo_update'),

   #======= Start_banner_api_url =======
   path('it/banner/', WebsiteBannerCreateit.as_view(), name='banner_create'),
   path('it/banner/<int:pk>/', WebsiteBannerUpdateit.as_view(), name='banner_update'),




   #======= Start_card_api_url_homepage_two =======

   path('it/card/two/one/', CardCreateHomepageTwoOneit.as_view(), name='card_create'),
   path('it/card/two/one/<int:pk>/', CardUpdateHomepageTwoOneit.as_view(), name='card_update'),

   path('it/card/two/', CardCreateHomepageTwoit.as_view(), name='card_create'),
   path('it/card/two/<int:pk>/', CardUpdateHomepageTwoit.as_view(), name='card_update'),




   #======= Start_card_api_url_homepage_three =======

   path('it/three/card/one/', CardCreateHomepageThreeOneit.as_view(), name='card_create_one'),
   path('it/three/card/one/<int:pk>/', CardUpdateHomepageThreeOneit.as_view(), name='card_update_one'),

   path('it/three/card/tow/', CardCreateHomepageThreeTwoit.as_view(), name='card_create'),
   path('it/three/card/tow/<int:pk>/', CardUpdateHomepageThreeTwoit.as_view(), name='card_update'),

   path('it/three/card/three/', CardCreateHomepageThreeit.as_view(), name='card_create'),
   path('it/three/card/three/<int:pk>/', CardUpdateHomepageThreeit.as_view(), name='card_update'),




   #======= Start_card_api_url_homepage_foure =======

   path('it/card/four/one/', CardCreateHomepageFourOneit.as_view(), name='card_create'),
   path('it/card/four/one/<int:pk>/', CardUpdateHomepageFourOneit.as_view(), name='card_update'),

   path('it/card/four/two/', CardCreateHomepageFourTwoit.as_view(), name='card_create'),
   path('it/card/four/two/<int:pk>/', CardUpdateHomepageFourTwoit.as_view(), name='card_update'),

   path('it/card/four/three/', CardCreateHomepageFourThreeit.as_view(), name='card_create'),
   path('it/card/four/three/<int:pk>/', CardUpdateHomepageFourThreeit.as_view(), name='card_update'),

   path('it/card/four/', CardCreateHomepageFourit.as_view(), name='card_create'),
   path('it/card/four/<int:pk>/', CardUpdateHomepageFourit.as_view(), name='card_update'),
   

   #======= Start_card_api_url_CardTemplate =======
   path('it/cardtemplate/', CardTemplateCreateit.as_view(), name='cardtemplate_create'),
   path('it/cardtemplate/<int:pk>/', CardTemplateUpdateit.as_view(), name='cardtemplate_update'),


   #======= Start_card_api_url_blogCard =======
   path('it/blogcard/', BlogCardCreateit.as_view(), name='card_create'),
   path('it/blogcard/<int:pk>/', BlogCardUpdateit.as_view(), name='card_detail'),

   #======= Start_Time_date_api_url_ =======
   path('it/datetime/', TimeDataCreateit.as_view(), name='datetime_create'),
   path('it/datetime/<int:pk>/', TimeDataUpdateit.as_view(), name='datetime_update'),

   #======= Start_Bank/MobileWallet_api_url_ =======
    path('it/bank/', BankCreateit.as_view(), name='bank-create'),
    path('it/bank/<int:pk>/', BankUpdateit.as_view(), name='bank-detail'),
    path('it/mobilewallet/', MobileWalletCreateit.as_view(), name='mobileWallet-create'),
    path('it/mobilewallet/<int:pk>/', MobileWalletUpdateit.as_view(), name='mobileWallet-detail'),

   #======= Start_OfflineBank_api_url_ =======
    path('it/offlinebank/', OfflineBankCreateit.as_view(), name='offline-bank-create'),
    path('it/offlinebank/<int:pk>/', OfflineBankUpdateit.as_view(), name='offline-bank-detail'),
    
    
    
    
    #======= Start_Homepage_Segment_api_url_ =======
    path('it/home-page-segment/', Homepage_Segmentit.as_view(), name='homepage_segment'),
    path('it/home-page-segment/<int:pk>/', Homepage_SegmentUpdateit.as_view(), name='homepage_segment_detail'),
    
    
    #======= Start_Support_Company_Logo_api_url_ =======
    path('it/company-logo/', Support_Company_Logoit.as_view(), name='company_logo'),
    path('it/company-logo/<int:pk>/', Support_Company_LogoUpdateit.as_view(), name='company_logo_detail'),
    
    
    #======= Start_Office_Address_api_url_ =======
    path('it/office-address-1/', Office_Address_1_it.as_view(), name='office_address_1'),
    path('it/office-address-1/<int:pk>/', Office_Address_1_Updateit.as_view(), name='office_address_1_detail'),
    path('it/office-address-2/', Office_Address_2_it.as_view(), name='office_address_2'),
    path('it/office-address-2/<int:pk>/', Office_Address_2_Updateit.as_view(), name='office_address_2_detail'),
    
    
    #======= Start_Payment_Logo_api_url_ =======
    path('it/payment-logo/', Payment_Logo_it.as_view(), name='payment_logo'),
    path('it/payment-logo/<int:pk>/', Payment_Logo_Updateit.as_view(), name='payment_logo_detail'),
    
    
    #======= Start_Social_Media_Link_api_url_ =======
    path('it/social-media/', Social_Media_it.as_view(), name='social_media'),
    path('it/social-media/<int:pk>/', Social_Media_Updateit.as_view(), name='social_media_detail'),
    
    
    #======= Start_Global_Location_api_url_ =======
    path('it/global-location/', Global_Location_it.as_view(), name='global_location'),
    path('it/global-location/<int:pk>/', Global_Location_Updateit.as_view(), name='global_location_detail'),
    
    
    #======= Start_Contact_Us_api_url_ =======
    path('it/contact-us/', Contact_Us_it.as_view(), name='contact_us'),
    path('it/contact-us/<int:pk>/', Contact_Us_Updateit.as_view(), name='contact_us_detail'),
    
    
    #======= Start_Subscribtions_api_url_ =======
    path('it/subscribtions/', Subscribtions_it.as_view(), name='subscribtions'),
    path('it/subscribtions/<int:pk>/', Subscribtions_Updateit.as_view(), name='subscribtions_detail'),
    
    
    
    #======= Start_Footer_Section_1_api_url_ =======
    path('it/footer-section-1/', Footer_Section_1_it.as_view(), name='footer_section_1'),
    path('it/footer-section-1/<int:pk>/', Footer_Section_1_Updateit.as_view(), name='footer_section_1_detail'),
    path('it/footer-1-topics/', Footer_Section_1_Topics_it.as_view(), name='footer_section_1_topics'),
    path('it/footer-1-topics/<int:pk>/', Footer_Section_1_Topics_Updateit.as_view(), name='footer_section_1_topics_detail'),
    
    
    #======= Start_Footer_Section_2_api_url_ =======
    path('it/footer-section-2/', Footer_Section_2_it.as_view(), name='footer_section_2'),
    path('it/footer-section-2/<int:pk>/', Footer_Section_2_Updateit.as_view(), name='footer_section_2_detail'),
    path('it/footer-2-topics/', Footer_Section_2_Topics_it.as_view(), name='footer_section_2_topics'),
    path('it/footer-2-topics/<int:pk>/', Footer_Section_2_Topics_Updateit.as_view(), name='footer_section_2_topics_detail'),
    
    
    #======= Start_Footer_Section_3_api_url_ =======
    path('it/footer-section-3/', Footer_Section_3_it.as_view(), name='footer_section_3'),
    path('it/footer-section-3/<int:pk>/', Footer_Section_3_Updateit.as_view(), name='footer_section_3_detail'),
    path('it/footer-3-topics/', Footer_Section_3_Topics_it.as_view(), name='footer_section_3_topics'),
    path('it/footer-3-topics/<int:pk>/', Footer_Section_3_Topics_Updateit.as_view(), name='footer_section_3_topics_detail'),
    
    
    #======= Start_Technology_api_url_ =======
    path('it/technology/', Technology_it.as_view(), name='technology'),
    path('it/technology/<int:pk>/', Technology_Updateit.as_view(), name='technology_detail'),
    path('it/technology-icon/', Technology_Icon_it.as_view(), name='technology_icon'),
    path('it/technology-icon/<int:pk>/', Technology_Icon_Updateit.as_view(), name='technology_icon_detail'),
    
    
    #======= Start_Our_Services_api_url_ =======
    path('it/our-services/', Our_Services_it.as_view(), name='our_services'),
    path('it/our-services/<int:pk>/', Our_Services_Updateit.as_view(), name='our_services_detail'),
    
    
    #======= Start_Notice_Board_api_url_ =======
    path('it/notice-board/', Notice_Board_it.as_view(), name='notice_board'),
    path('it/notice-board/<int:pk>/', Notice_Board_Updateit.as_view(), name='notice_board_detail'),
    
    
    #======= Start_Security_Page_api_url_ =======
    path('it/security-page/', Security_Page_it.as_view(), name='security_page'),
    path('it/security-page/<int:pk>/', Security_Page_Updateit.as_view(), name='security_page_detail'),
    
    
    #======= Start_Order_Card_api_url_ =======
    path('it/order-card/', Order_Card_it.as_view(), name='order_card'),
    path('it/order-card/<int:pk>/', Order_Card_Updateit.as_view(), name='order_card_detail'),
    
    
    #======= Start_Company_Member_api_url_ =======
    path('it/company-member/', Company_Member_it.as_view(), name='company_member'),
    path('it/company-member/<int:pk>/', Company_Member_Updateit.as_view(), name='company_member_detail'),
    
    
]
