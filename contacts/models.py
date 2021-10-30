from django.db import models
# importing validationerror
# from django.core.exceptions import ValidationError



# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10,blank = False, null = False)
    address = models.CharField(max_length=1000)

    def __str__(self):
          return self.full_name

