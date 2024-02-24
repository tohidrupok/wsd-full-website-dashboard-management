from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Admin_User

# ==========Admin User Creation Serializer Start==========
class AdminUserCreationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})

    class Meta:
        model = Admin_User
        fields = ['name', 'email', 'username', 'user_type', 'password1', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password1(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = Admin_User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            username=validated_data['username'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user
# ==========Admin User Creation Serializer End==========

from django.contrib.auth import authenticate, login
# ==========User Login Serializer Start==========
class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if Admin_User.objects.filter(username=username).exists():
            if authenticate(username=username, password=password):
                return data
            else:
                raise serializers.ValidationError("Invalid Password!")
        else:
            raise serializers.ValidationError("Invalid Username This yet!")



class AdminOTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate_otp(self, value):
        otp = int(value)
        stored_otp = self.context['request'].session.get('admin_login_otp')
        if otp == stored_otp:
            return value
        else:
            raise serializers.ValidationError("OTP does not match.")
# ==========User Login Serializer End==========


# ==========Password Reset Serializer Start==========
class AdminForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not Admin_User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email does not exist in our database.")
        return value

class AdminResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    password1 = serializers.CharField(max_length=50)
    password2 = serializers.CharField(max_length=50)

    def validate_otp(self, value):
        stored_otp = self.context['request'].session.get('admin_reset_password_otp')
        if int(value) != stored_otp:
            raise serializers.ValidationError("OTP doesn't match.")
        return value
    
    def validate_email(self, value):
        stored_email = self.context['request'].session.get('admin_reset_password_email')
        if value != stored_email:
            raise serializers.ValidationError("Wrong Email.")
        return value

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Password and Confirm Password don't match.")
        return data
# ==========Password Reset Serializer End==========


# ==========Password Change Serializer Views Start==========
class AdminChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50, write_only=True)
    new_password1 = serializers.CharField(label='New Password', max_length=50, write_only=True)
    new_password2 = serializers.CharField(label='New Confirm Password', max_length=50, write_only=True)
# ==========Password Change Serializer Views End==========


