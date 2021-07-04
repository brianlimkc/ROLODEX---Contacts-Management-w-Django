from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(
    primary_key=True,
    editable=False,
    default=uuid.uuid4
    )
    name = models.CharField(max_length=200, null=False) 
    gender = models.CharField(max_length=10, default="")     
    race = models.CharField(max_length=40, default="") 
    birthday = models.CharField(max_length=20, default="") 
    street = models.CharField(max_length=100, default="") 
    city = models.CharField(max_length=100, default="")          
    email = models.EmailField(default="")
    phone_number = models.CharField(max_length=20, default="")
    mobile_number = models.CharField(max_length=20, default="")

    
    def __str__(self):
        return self.name
