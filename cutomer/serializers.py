from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ["id", "name", "email", "mobile", "password"]
        fields = "__all__"
        extra_kwargs  = {
            "password":{"write_only":True}
        }
        
    def validate_mobile(self, value):
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("mobile no must 10 digits")
        return value
        
    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("email only allow gmail")
        return value
    
    def create(self, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
    
    # def validat_password(self, value):
    #     if "password" in value:
    #         value['password'] = make_password(value['password'])
    #     return super().create(value)    
               
class CustomerResetPass(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True, min_length=4)
    password = serializers.CharField(write_only=True)
    
    
    # def validate_email(self, value):
    #     if not Customer.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("No user found with this email.")
    #     return value
    
    # def save(self, **kwargs):
    def save(self, **kwargs):
        email = self.validated_data.get("email")
        password = self.validated_data.get('password')
        new_password = self.validated_data.get("new_password")
        print("email", email)
        user = Customer.objects.get(email = email)
        print("email1",user.email)
        print("password1",password)
        passs=user.password
        if not check_password(password, passs):
            print("password", password)   
            return serializers.ValidationError("old password is not match")
        user.password = make_password(new_password)
        user.save()
        return user
              
class CustomerForgotPass(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def save(self, **kwargs):
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")  
        
        user = Customer.objects.get(email=email)
        user.password = make_password(password)
        user.save()
        return user     