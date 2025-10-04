from django.db import models
from django.contrib.auth.models import User



class category(models.Model):
    category=models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.category

# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    post_category=models.ManyToManyField(category)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


    class Meta:
        ordering=['-date']


