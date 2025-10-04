from django.contrib.auth.models import User
from django.db import models
from django.template.context_processors import request


# Create your models here.


class contact_us(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField()
        title = models.CharField(max_length=50)
        body = models.TextField()
        user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

        def __str__(self):
           return self.title
