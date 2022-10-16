from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Messages(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    subject = models.CharField(max_length = 50, null = True, blank = True)
    message = models.TextField(max_length = 500, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)