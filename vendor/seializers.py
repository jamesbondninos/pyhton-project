from rest_framework import serializers
from .models import vendorCreatation
from datetime import date

class VendorSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = vendorCreatation
        # fields = ["name","dob", "age"]
        fields = '__all__'
        
    def get_age(self, obj):
        if obj.dob:
          print("obj", obj)
          print("obj.dob", obj.dob)
          today = date.today()
          age = today.year - obj.dob.year
        
          if(today.month, today.day) < (obj.dob.month, obj.dob.day):
            age -= 1
          return age  