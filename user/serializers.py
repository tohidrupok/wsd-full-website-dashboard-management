from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import *


# ==============================
# Serializers For Website User Registration And Verficiation
# ==================================
class UserCreationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Website_User
        fields = ['full_name', 'email', 'username', 'country', 'gender', 'password1', 'password2']

    def validate_password1(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match!")
        return data

    def create(self, validated_data):
        user = Website_User.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            country=validated_data['country'],
            gender=validated_data['gender'],
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user
  
class UserVerificationSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)
    def validate_otp(self, value):
        otp = int(value)
        stored_otp = self.context['request'].session.get('account_verify_otp')
        if otp == stored_otp:
            return value
        else:
            raise serializers.ValidationError("OTP does not match.")


# =============== Serializers For Website User Profile ===================
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


# =========== Serializers For Website User Company Information ===============
class CompanyInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInformation
        fields = '__all__'

# ========== Serializers For Website User Contact Information ==============
class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'

# ================ Serializers For Website User Social Link ====================
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

# ================= Serializers For Website User Address =====================
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'



# ==========Password Change Serializer Views Start==========
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50, write_only=True)
    new_password1 = serializers.CharField(label='New Password', max_length=50, write_only=True)
    new_password2 = serializers.CharField(label='New Confirm Password', max_length=50, write_only=True)
# ==========Password Change Serializer Views End==========

from django.contrib.auth import authenticate
# ==========User Login Serializer Start==========
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, write_only=True)
    password = serializers.CharField(max_length=50, write_only=True, style={'input_type': 'password'})
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if Website_User.objects.filter(username=username).exists():
            if authenticate(username=username, password=password):
                website_user = Website_User.objects.get(username=username)
                if website_user.is_varified != True:
                    raise serializers.ValidationError("This account is not varified!")
                if website_user.is_delete == True:
                    raise serializers.ValidationError("This account was deleted!")
                else:
                    return attrs
            else:
                raise serializers.ValidationError("Invalid Password!")
        else:
            raise serializers.ValidationError("Invalid Username is yet!")
    
# ==========User Login Serializer End==========


# ==========Password Reset Serializer Start==========
class ForgetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        if not Website_User.objects.filter(username=username, email=email).exists():
            raise serializers.ValidationError("Account does not exist in our database.")
        return data

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    password1 = serializers.CharField(max_length=50, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=50, style={'input_type': 'password'}, write_only=True)

    def validate_otp(self, value):
        stored_otp = self.context['request'].session.get('user_reset_password_otp')
        if int(value) != stored_otp:
            raise serializers.ValidationError("OTP doesn't match.")
        return value

    def validate(self, data):
        stored_email = self.context['request'].session.get('user_reset_password_email')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Password and Confirm Password don't match.")
        elif stored_email != email:
            raise serializers.ValidationError("Wrong Email.")
        return data
# ==========Password Reset Serializer End==========



