from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = User.objects.create_user(username=name, email=email, password=password)
        login(request, user)
        
        return redirect('zakapp:index')
    
    return render(request, 'zakapp/register.html')

def view_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        username = User.objects.get(email=email).username
       
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            redi = redirect('zakapp:index')
            redi.set_cookie('email', user.email, max_age=60*60)
            
            login(request, user)
            
            return redi
        
        else:
            context = {
                'email': email,
                'status': False,
            }
            
            return render(request, 'zakapp/login.html', context)
    
    return render(request, 'zakapp/login.html')

def view_logout(request):
    logout(request)
    
    return redirect('zakapp:index')

def index(request):
    return render(request, 'zakapp/index.html')
