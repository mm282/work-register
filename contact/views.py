from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from .models import contact_us
from django.contrib.auth import authenticate


# Create your views here.


def contact(request):
    context={'errore':[]}
    if request.method == "POST":

       name= request.POST.get('name')
       email = request.POST.get('email')
       title = request.POST.get('title')
       body = request.POST.get('body')
       user=request.user
       #
       if request.user.is_authenticated:
           contact_us.objects.create(name=name, email=email, title=title, body=body, user=user)



       else:
           return redirect('login:login')

    return render(request, 'contact/contact.html',context)
