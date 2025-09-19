from rest_framework import serializers
from .models import CustomUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "name", "email", "mobile"]
        
    def validate_mobile(self, value):
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("mobile no must 10 digits")
        return value 
        
    def validate_email(self, value):
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("only gmail are allowed")
        return value 