from django.db import models
from datetime import date

# Create your models here.
class vendorCreatation(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # mobile = models.IntegerField(max_length=10, unique=True)
    # email = models.EmailField(unique=True)
    
    
    # def age(self):
    #     today = date.today()
    #     age = today.year - self.dob.year
        
    #     if(today.month, today.day) < (self.dob.month, self.dob.day):
    #         age -= 1
    #     return age  
      
    def __str__(self):
        return self.name