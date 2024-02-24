from django.db import models


# =================Website Logo Section Start=======================
class Civil_WebsiteLogo(models.Model):
    image = models.ImageField(upload_to='civil/image/logo/',blank=True, null=True)
    def __str__(self):
        return f"{self.image.name}"
# =================Website Logo Section End=======================


# =================Website Banner Section Start=======================
class Civil_WebsiteBanner(models.Model):
    header = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    image_and_video = models.FileField(upload_to='civil/image/banners/', blank=True, null=True)

    def __str__(self):
        return f"{self.header} - {self.tag}"
# =================Website Banner Section End=======================

# =================Website 2 Card Section Start=======================
class Civil_CardHomepageTwoOne(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"

class Civil_CardHomepageTwo(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"
# =================Website 2 Card Section End=======================


# =================Website Three Card Section Start=======================
class Civil_CardHomepageThreeOne(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"

class Civil_CardHomepageThreeTwo(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"

class Civil_CardHomepageThree(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"
# =================Website Three Card Section End=======================


# =================Website Four Card Section Start=======================
class Civil_CardHomepageFourOne(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"

class Civil_CardHomepageFourTwo(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"

class Civil_CardHomepageFourThree(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"

class Civil_CardHomepageFour(models.Model):
    icon = models.ImageField(upload_to='civil/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag} - {self.description}"
# =================Website Four Card Section End=======================

# =================Website Template Card Section Start=======================
class Civil_CardTemplate(models.Model):
    image = models.ImageField(upload_to='civil/image/card_images/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    url = models.URLField()
    
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.image} - {self.title} - {self.tag} - {self.price} - {self.url}"
# =================Website Template Card Section End=======================


# =================Website Blog Card Section Start=======================
class Civil_BlogCard(models.Model):
    image = models.ImageField(upload_to='civil/image/blog_images/',blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField()
    
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.image} - {self.title} - {self.tag} - {self.description}"
# =================Website Blog Card Section End=======================

# =================Website Timedata Section Start=======================
class Civil_TimeData(models.Model):
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    hour = models.PositiveSmallIntegerField()
    second = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.second}"
# =================Website Timedata Section End=======================

# =================Website Segment Section Start=======================
class Civil_Homepage_Segment(models.Model):
    photo_or_video = models.FileField(upload_to='civil/image/segment/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.photo_or_video.name
# =================Website Segment Section End=======================


# =================Website Company Logo Section Start=======================
class Civil_Support_Company_Logo(models.Model):
    logo = models.ImageField(upload_to='civil/image/comapny-logo/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.logo.name
# =================Website Company Logo Section End=======================

# Tow Office Address Section Models Start================
class Civil_Office_Address_1(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.address} - {self.email} - {self.phone} - {self.fax}'

class Civil_Office_Address_2(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.address} - {self.email} - {self.phone} - {self.fax}'
# Tow Office Address Section Models End================

# =================Website Payment Logo Section Start=======================
class Civil_Payment_Logo(models.Model):
    logo = models.ImageField(upload_to='civil/image/payment-logo/', blank=True, null=True)

    def __str__(self) -> str:
        return self.logo.name
# =================Website Payment Logo Section End=======================

# =================Website Social Media Section Start=======================
class Civil_Social_Media(models.Model):
    icon = models.ImageField(upload_to='civil/image/socialmedia-icon/', blank=True, null=True)
    url = models.URLField(max_length=500)
    
    def __str__(self) -> str:
        return self.icon.name
# =================Website Social Media Section End=======================


# =================Website Global Location Section Start=======================
class Civil_Global_Location(models.Model):
    flag_logo = models.ImageField(upload_to='civil/image/global-location-flag/', blank=True, null=True)
    country_name = models.CharField(max_length=30)
    office_address = models.CharField(max_length=400)
    contact_details = models.CharField(max_length=400)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.country_name
# =================Website Global Location Section End=======================

# =================Website Contact Section Start=======================
class Civil_Contact_Us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=600)
    message = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.name} - {self.email} - {self.phone_number} - {self.subject}'
# =================Website Contact Section End=======================

# =================Website Subscription Section Start=======================
class Civil_Subscriptions(models.Model):
    email = models.EmailField(max_length=150)
    
    def __str__(self) -> str:
        return self.email
# =================Website Subscription Section End=======================


# ===========================Footer Section 1 Start=================================
class Civil_Footer_Section_1(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
class Civil_Footer_Section_1_Topics(models.Model):
    footer_section = models.ForeignKey(Civil_Footer_Section_1, on_delete=models.CASCADE, related_name='footer_section_1_topics')
    topic_name = models.CharField(max_length=50)
    topic_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.footer_section.title} - {self.topic_name}'
# ===========================Footer Section 1 End=================================


# ===========================Footer Section 2 Start=================================
class Civil_Footer_Section_2(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
class Civil_Footer_Section_2_Topics(models.Model):
    footer_section = models.ForeignKey(Civil_Footer_Section_2, on_delete=models.CASCADE, related_name='footer_section_2_topics')
    topic_name = models.CharField(max_length=50)
    topic_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.footer_section.title} - {self.topic_name}'
# ===========================Footer Section 2 End=================================


# ===========================Footer Section 3 Start=================================
class Civil_Footer_Section_3(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
class Civil_Footer_Section_3_Topics(models.Model):
    footer_section = models.ForeignKey(Civil_Footer_Section_3, on_delete=models.CASCADE, related_name='footer_section_3_topics')
    topic_name = models.CharField(max_length=50)
    topic_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.footer_section.title} - {self.topic_name}'
# ===========================Footer Section 3 End=================================


# ===========================Technology Start=================================
class Civil_Technology(models.Model):
    name = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name

class Civil_Technology_Icon(models.Model):
    technology = models.ForeignKey(Civil_Technology, on_delete=models.CASCADE, blank=True, null=True)
    icon = models.ImageField(upload_to='civil/image/technology-icons/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.technology.name} - {self.icon.name}'
# ===========================Technology End=================================


# ===========================Our Services Start=================================
class Civil_Our_Services(models.Model):
    icon = models.ImageField(upload_to='civil/image/services-icons/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
        return self.title
# ===========================Our Services End=================================


# ===========================Notice Board Start=================================
class Civil_Notice_Board(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    status = models.CharField(max_length=50)
    file = models.FileField(upload_to='civil/image/notice-board/', blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.date} - {self.title}'
# ===========================Notice Board End=================================


# ===========================Order Card Start=================================
class Civil_Order_Card(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='civil/image/order-card/', blank=True, null=True)
    file = models.FileField(upload_to='civil/image/order-card/', blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
# ===========================Order Card End=================================


# ===========================Security Page Model Start=================================
class Civil_Security_Page(models.Model):
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.description
# ===========================Security Page Model End=================================


# ===========================Company Member Start=================================
class Civil_Company_Member(models.Model):
    image = models.ImageField(upload_to='civil/image/company-member/', blank=True, null=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
# ===========================Company Member End=================================


