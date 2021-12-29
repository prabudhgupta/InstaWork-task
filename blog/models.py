from django.db import models
from django.db.models.fields import BooleanField
from phonenumber_field.modelfields import PhoneNumberField

ROlE = (
   ('R', 'Regular-cant delete members'),
   ('A', 'Admin-can delete members')
)



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number = PhoneNumberField(null=False, blank=False, unique=True)
    role = models.CharField(max_length=128)
    

class user_form(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length= 255)
    email = models.EmailField(max_length=255,)
    number = PhoneNumberField(null=False, blank=False)
    role = models.CharField(max_length=128)
    class Meta:  
        db_table = "user_form"  
    

