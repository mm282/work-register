from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from home.urls import app_name


# Create your views here.


def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    return render(request, 'login/index.html')


def user_logout(request):
    logout(request)
    return redirect('/')



def register(request):
    context={"errore":[]}


    if request.method == "POST":

        usernsme = request.POST.get("username")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")


        if password2 == password:

            User.objects.create_user(username=usernsme, password=password)
            context["errore"].append('Passwords are not same')
            return redirect("/")







        else:
            context["errore"].append('رمز ها مشابه نیستند')
            print(context)

    return render(request, 'login/register.html',context)



def user_detail(request):
    users=request.user
    return render(request,'login/user_detail.html',context={'user':users})
