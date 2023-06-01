from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class UserCustom(models.Model):
#     userID = models.AutoField(User, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=254, unique=True)
#     username = models.CharField(max_length=254, unique=True)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.username}"
     
class EmailMetadata(models.Model):
    primary_key = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_email = models.EmailField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.primary_key}: {self.userID}"
    

