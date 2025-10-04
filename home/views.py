from django.shortcuts import render
from post.models import Article,category
# Create your views here.


def home (request):
    sidbar_articles=Article.objects.all()[:3]
    sidbar_category=category.objects.all()


    article=Article.objects.all()[:2]
    return render (request,'home/index.html',context={'article':article,'sidbar_articles':sidbar_articles,'sidbar_category':sidbar_category})