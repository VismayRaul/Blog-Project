from email.policy import default
from site import USER_BASE
from urllib.parse import uses_query
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userimg(models.Model):
    actuser = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_img',default='',blank=True,null=True)
    def __str__(self):
        return self.actuser

class Blogs(models.Model):
    activeuser = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    blogtitle = models.CharField(max_length=50)
    intro = models.CharField(max_length=225)
    discription = models.TextField()
    blogimage = models.ImageField(upload_to='blog_img',default=0)
    relatedfile = models.FileField(upload_to='files/',null=True)


    def __str__(self):
        return self.blogtitle + ": " + str(self.relatedfile)