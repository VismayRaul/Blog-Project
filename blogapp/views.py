from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required(login_url='signin')
def home(request):
    return render(request,'home.html')

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
        createUser = User.objects.create_user(username,email,pass1)
        createUser.first_name = username
        createUser.save()
        messages.success(request,"Your account has been created successfully")
        return redirect('signin')
    return render(request,'signup.html')

def signout(request):
    logout(request)
    return redirect('index')

def detail_blog(request):
    return render(request,'detail_blog.html')