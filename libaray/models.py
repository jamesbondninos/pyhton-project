from django.db import models
from datetime import date

# Create your models here.
class libaray(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dod = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
