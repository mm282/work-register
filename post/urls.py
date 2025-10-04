from django.urls import path
from . import views


app_name='post'

urlpatterns= [
    path('',views.blog,name='blog'),
    path('post/<int:id>',views.detail,name='detail'),
    path('search', views.search, name='search'),
    path('add', views.register_post, name='add'),

]