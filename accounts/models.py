from django.contrib.auth.models import AbstractUser 
from django.db import models
from shop.models import City

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    city = models.ForeignKey(City,default='', null=True, blank=False ,on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.city
    