from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username =models.EmailField(max_length=200,blank=True,null=True)
    short_intro=models.CharField(max_Length=200,blank=True,null=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default="profiles/bhai11.jpg")
    social_github = models.CharField(max_Length=200,blank=True,null=True) 
    social_twitter = models.CharField(max_Length=200,blank=True,null=True)
    social_youtube= models.CharField(max_Length=200,blank=True,null=True)
    social_linkedin = models.CharField(max_Length=200,blank=True,null=True)
    social_website = models.CharField(max_Length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return str(self.user.username)