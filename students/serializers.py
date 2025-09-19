from rest_framework import serializers
from .models import Students

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name', 'email', 'password']
        write_only_fields=['password']
        
class StudentsSerialLogin(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'password']        