from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        # https://docs.djangoproject.com/en/5.0/topics/auth/default/#authenticating-users
        user = authenticate(username=username, password=password)
        
        if user is not None :
            # https://docs.djangoproject.com/en/5.0/topics/auth/default/#how-to-log-a-user-in
            login(request, user)
            return redirect('authapp:index')
        else :
            # 유저 인증 실패
            context = {
                'username': username,
                'status': False,
            }
            return render(request, 'signin.html', context)

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        User.objects.create_user(username=username, password=password)

        return redirect('authapp:index')
    
def signout(request):
    logout(request)
    return redirect('authapp:index')