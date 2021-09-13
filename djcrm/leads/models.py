from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    

class Lead(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Agent(models.Model):
    user =  models.OneToOneField(User, on_delete=CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    