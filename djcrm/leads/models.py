from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save,pre_save
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
    
def post_user_created_signal(sender,instance,created, **kwargs):
    print(instance,created)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal,sender=User)
