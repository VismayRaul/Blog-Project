from re import template
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Blogs,Userimg
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader

from django.db.models import Q

from blogapp.models import Blogs
# Create your views here.

def index(request):
    blog = Blogs.objects.all().values()
    if 'search' in request.GET:
        search = request.GET['search']
        multiple_search = Q(Q(blogtitle__icontains = search) | Q(intro__icontains = search))
        blog = Blogs.objects.filter(multiple_search)
    else:
        blog = Blogs.objects.all()
        
    return render(request,'index.html',context={'blog':blog})

@login_required(login_url='signin')
def home(request):
    blog = Blogs.objects.all().values()
    if 'search' in request.GET:
        search = request.GET['search']
        multiple_search = Q(Q(blogtitle__contains = search) | Q(intro__contains = search))
        blog = Blogs.objects.filter(multiple_search)
    else:
        blog = Blogs.objects.all()
    return render(request,'home.html', context={'blog':blog})

def profile(request):
    blog = Blogs.objects.all().values()

    if 'search' in request.GET:
        search = request.GET['search']
        multiple_search = Q(Q(blogtitle__icontains = search) | Q(intro__icontains=search))
        blog = Blogs.objects.filter(multiple_search)
    else:
        blog = Blogs.objects.all()
        
    return render(request,'profile.html',context={'blog':blog })

def profile_form(request):
    if request.method == 'POST':
        activeuser = request.user.username
        title = request.POST['blogtitle']
        intro = request.POST['intro']
        discription = request.POST['discription']
        blogimage = request.POST['blogimage']
        blogfile = request.POST['relatedfile']
        print(blogimage)

        # Blogs.objects.select_for_update(activeuser)
        blogs = Blogs.objects.create(blogtitle=title,intro=intro,discription=discription,blogimage=blogimage,relatedfile=blogfile)
        blogs.save()
        return redirect('profile')
    return render(request,'profile_form.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('home')
        else:
            messages.error(request,"Username or password invalid")

    return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        image = request.POST['image']
        userimg = Userimg.objects.create(image=image)
        # userimg.actuser = username
        userimg.save()
        createUser = User.objects.create_user(username,email,pass1)
        createUser.first_name = username
        createUser.save()
        messages.success(request,"Your account has been created successfully")
        return redirect('signin')
    return render(request,'signup.html')

def signout(request):
    logout(request)
    return redirect('index')

def detail_blog(request,id):
    blog = Blogs.objects.filter(id=id)
    return render(request,'detail_blog.html',context={'blog':blog})

def delete(request,id):
    Blogs.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('profile'))

def deleteprofile(request,id):
    User.objects.filter(id=id).delete()
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def edit(request,id):
    myblog = Blogs.objects.get(id=id)
    template = loader.get_template('editblog.html')
    context={
        'myblog':myblog
    }
    return HttpResponse(template.render(context,request))
    
def edited(request,id):
    title = request.POST['blogtitle']
    intro = request.POST['intro']
    discription = request.POST['discription']
    blogimage = request.POST['blogimage']
    blogfile = request.POST['relatedfile']
    Blogs.objects.filter(id=id).update(blogtitle=title,intro=intro,discription=discription,blogimage=blogimage,relatedfile=blogfile)
    return HttpResponseRedirect(reverse('profile'))