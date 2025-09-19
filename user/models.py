from django.db import models

# Create your models here.

class CustomUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.name