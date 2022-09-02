from django.urls import path
from .views import *
from . import views
urlpatterns= [
    path('',index,name='index'),
    path('home',home,name='home'),
    path('signin',signin,name='signin'),
    path('signup',signup,name='signup'),
    path('signout',signout,name='signout'),
    path('detail_blog/<int:id>',views.detail_blog,name='detail_blog'),
    path('profile',profile,name='profile'),
    path('profile_form',profile_form,name='profile_form'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('edit/edited/<int:id>',views.edited,name='edited'),
    path('deleteprofile/<int:id>',views.deleteprofile,name='deleteprofile'),
]