from django.shortcuts import render
from django.core.paginator import Paginator
from post.models import Article, category


# Create your views here.
def blog(request):
    article = Article.objects.all()
    sidbar_articles = Article.objects.all()[:3]
    page_number = request.GET.get("page")
    paginator = Paginator(article, 2)
    object = paginator.get_page(page_number)
    return render(request, "post/blog.html", context={'object': object, 'sidbar_articles': sidbar_articles})


def detail(request, id):
    sidbar_articles = Article.objects.all()[:3]
    article = Article.objects.get(id=id)
    return render(request, "post/post-details.html", context={'article': article, 'sidbar_articles': sidbar_articles})


def search(request):
    q = request.GET.get('q')
    object = Article.objects.filter(name__contains=q)
    return render(request, "post/search.html", context={'object': object})


def register_post(request):
    name = request.POST.get('name')
    body = request.POST.get('body')
    category1 = request.POST.get('category')
    user=request.user
    category2=category.objects.all()
    if category1 is not None:
        m, created = category.objects.get_or_create(category=category1)


        article = Article.objects.create(name=name, body=body, author=user)
        article.post_category.add(m)

    return render(request, "post/registerpost.html",context={'category2':category2})

