from django.db import models


class WebsiteLogo(models.Model):
    image = models.ImageField(upload_to='static/image/logo/',blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.image.name} - {self.description}"

class WebsiteBanner(models.Model):
    header_text = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    image_and_video = models.FileField(upload_to='static/image/banners/', blank=True, null=True)

    def __str__(self):
        return f"{self.header_text} - {self.tag_text}"






class CardHomepageTwoOne(models.Model):
    icon = models.ImageField(upload_to='static/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"
    

class CardHomepageTwo(models.Model):
    icon = models.ImageField(upload_to='static/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"
    

class CardHomepageThreeOne(models.Model):
    icon = models.ImageField(upload_to='static/three/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"


class CardHomepageThreeTwo(models.Model):
    icon = models.ImageField(upload_to='static/three/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"


class CardHomepageThree(models.Model):
    icon = models.ImageField(upload_to='static/three/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"
 

class CardHomepageFourOne(models.Model):
    icon = models.ImageField(upload_to='static/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"


class CardHomepageFourTwo(models.Model):
    icon = models.ImageField(upload_to='static/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"


class CardHomepageFourThree(models.Model):
    icon = models.ImageField(upload_to='static/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"


class CardHomepageFour(models.Model):
    icon = models.ImageField(upload_to='static/image/icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.icon} - {self.title} - {self.tag_text} - {self.description}"




class CardTemplate(models.Model):
    image = models.ImageField(upload_to='static/image/card_images/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    url = models.URLField()

    def __str__(self):
        return f"{self.image} - {self.title} - {self.tag} - {self.price} - {self.url}"


class BlogCard(models.Model):
    image = models.ImageField(upload_to='static/image/blog_images/',blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.image} - {self.title} - {self.tag} - {self.description}"


class TimeData(models.Model):
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    hour = models.PositiveSmallIntegerField()
    second = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.second}"





class Bank(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='static/image/bank_icons/')
    qr_code = models.ImageField(upload_to='static/image/bank_qr_codes/')
    account_details = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.icon}-{self.qr_code} {self.account_details}:{self.active}"

class MobileWallet(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='static/image/mobile_wallet_icons/')
    qr_code = models.ImageField(upload_to='static/image/mobile_wallet_qr_codes/')
    account_details = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.icon}-{self.qr_code} {self.account_details}:{self.active}"


class OfflineBank(models.Model):
    country_name = models.CharField(max_length=100)
    payment_person = models.CharField(max_length=100)
    payment_person_id = models.CharField(max_length=100)
    check_number = models.CharField(max_length=100)
    check_security_code = models.CharField(max_length=100)
    currency_iso = models.CharField(max_length=3)
    check_account = models.CharField(max_length=100)
    status = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.country_name}-{self.payment_person}-{self.payment_person_id} {self.check_number}:{self.check_security_code}-{self.currency_iso} {self.check_account}:{self.status}"







class Homepage_Segment(models.Model):
    photo_or_video = models.FileField(upload_to='static/image/segment/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.photo_or_video.name



class Support_Company_Logo(models.Model):
    logo = models.ImageField(upload_to='static/image/comapny-logo/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.logo.name


class Office_Address_1(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.address} - {self.email} - {self.phone} - {self.fax}'

class Office_Address_2(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.address} - {self.email} - {self.phone} - {self.fax}'


class Payment_Logo(models.Model):
    logo = models.ImageField(upload_to='static/image/payment-logo/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.logo.name

class Social_Media(models.Model):
    icon = models.ImageField(upload_to='static/image/socialmedia-icon/', blank=True, null=True)
    url = models.URLField(max_length=500)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.icon.name


class Global_Location(models.Model):
    flag_logo = models.ImageField(upload_to='static/image/global-location-flag/', blank=True, null=True)
    country_name = models.CharField(max_length=30)
    office_address = models.CharField(max_length=400)
    contact_details = models.CharField(max_length=400)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.country_name


class Contact_Us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=600)
    message = models.TextField()
    
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.email} - {self.phone_number} - {self.subject}'


class Subscribtions(models.Model):
    email = models.EmailField(max_length=150)
    
    def __str__(self) -> str:
        return self.email



# ===========================Footer Section 1 Start=================================
class Footer_Section_1(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
class Footer_Section_1_Topics(models.Model):
    section = models.ForeignKey(Footer_Section_1, on_delete=models.CASCADE, related_name='section_1_topics')
    topic = models.CharField(max_length=50)
    topic_url = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.section.title} - {self.topic}'
# ===========================Footer Section 1 End=================================

# ===========================Footer Section 2 Start=================================
class Footer_Section_2(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
class Footer_Section_2_Topics(models.Model):
    section = models.ForeignKey(Footer_Section_2, on_delete=models.CASCADE, related_name='section_2_topics')
    topic = models.CharField(max_length=50)
    topic_url = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.section.title} - {self.topic}'
# ===========================Footer Section 2 End=================================

# ===========================Footer Section 3 Start=================================
class Footer_Section_3(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
class Footer_Section_3_Topics(models.Model):
    section = models.ForeignKey(Footer_Section_3, on_delete=models.CASCADE, related_name='section_3_topics')
    topic = models.CharField(max_length=50)
    topic_url = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.section.title} - {self.topic}'
# ===========================Footer Section 3 End=================================


# ===========================Technology Start=================================
class Technology(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

class Technology_Icon(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, blank=True, null=True)
    icon = models.ImageField(upload_to='static/image/technology-icons/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.technology.name} - {self.icon.name}'
# ===========================Technology End=================================


# ===========================Services Start=================================
class Our_Services(models.Model):
    icon = models.ImageField(upload_to='static/image/services-icons/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
# ===========================Services End=================================


# ===========================Notice Board Start=================================
class Notice_Board(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    status = models.CharField(max_length=50)
    file = models.FileField(upload_to='static/image/notice-board/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.date} - {self.title}'
# ===========================Notice Board End=================================


# ===========================Order Card Start=================================
class Order_Card(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/image/order-card/', blank=True, null=True)
    file = models.FileField(upload_to='static/image/order-card/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
# ===========================Order Card End=================================

# ===========================Security Page Model Start=================================
class Security_Page(models.Model):
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.description
# ===========================Security Page Model End=================================

# ===========================Company Member Start=================================
class Company_Member(models.Model):
    image = models.ImageField(upload_to='static/image/company-member/', blank=True, null=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
# ===========================Company Member End=================================





