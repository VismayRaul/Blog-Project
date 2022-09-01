from django.urls import path
from .views import *

urlpatterns= [
    path('',index,name='index'),
    path('home',home,name='home'),
    path('signin',signin,name='signin'),
    path('signup',signup,name='signup'),
    path('signout',signout,name='signout'),
    path('detail_blog',detail_blog,name='detail_blog'),
]