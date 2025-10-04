from django.urls import path
from . import views

app_name="login"

urlpatterns =[
    path('',views.user_login,name='login'),
    path('register', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('detail/', views.user_detail, name='user_detail'),

]