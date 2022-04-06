from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Blogmodel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=200)
    Newpost=models.TextField(max_length=10000)
    summary=models.TextField(max_length=200,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title},{self.Newpost},{self.published_date},{self.created_date}'

class commentmodel(models.Model):
    blogmodel=models.ForeignKey(Blogmodel,related_name='comments' ,on_delete=models.CASCADE,blank=True,null=True)
    comment=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated=models.DateTimeField(auto_now=True,blank=True)
    active=models.BooleanField(default=True,blank=True)
    def __str__(self):
        return f'{self.comment},'

    class Meta:
        ordering=['created']

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return f'{self.user}'

