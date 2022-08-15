from django.db import models
from phone_field import PhoneField


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = PhoneField(blank=True, help_text='Contact phone number')
    #number = models.IntegerField()