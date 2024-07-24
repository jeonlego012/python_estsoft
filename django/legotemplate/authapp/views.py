from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import UserLoginModelForm, UserRegisterForm, UserChangePasswordForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        userform = UserLoginModelForm(request.POST)
        print(f'result!!! {request.POST["username"]} /// {userform.data["username"]}')
        
        username = userform.data["username"]
        password = userform.data["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('index:index')
    else:
        userform = UserLoginModelForm(label_suffix='')

    context = {
        'userform': userform,
    }
    return render(request, 'authapp/login.html', context)

def register(request):
    if request.method == "POST":
        '''
        userform = UserRegisterModelForm(request.POST)
    
        email = userform.data["email"]
        username = userform.data["username"]
        password = userform.data["password"]
        
        user = User.objects.create_user(email=email, username=username, password=password)
        login(request, user)
        
        return redirect('index:index')
        '''
        
        userform = UserRegisterForm(request.POST)

        email = userform.data["email"]
        username = userform.data["username"]
        password = userform.data["password"]
        password2 = userform.data["password2"]
        
        if password == password2:
            user = User.objects.create_user(email=email, username=username, password=password)
            login(request, user)
            
            return redirect('index:index')
            
        else:
            userform = UserRegisterForm(label_suffix='')
        
    else:
        userform = UserRegisterForm(label_suffix='')
    
    context = {
        'userform': userform,
    }
    return render(request, 'authapp/register.html', context)

def changePassword(request):
    if request.method == "POST":
        
        userform = UserChangePasswordForm(request.POST)
        email = userform.data["email"]
        password = userform.data["password"]
        password2 = userform.data["password2"]
        
        user = User.objects.get(email=email)
        print(f"result!! {email} {password} {password2} {user.username}")
        
        if password == password2:
            user.password = password
            user.save()
            
            return redirect('index:index')
    else:
        userform = UserChangePasswordForm(label_suffix='')
    
    context = {
        'userform': userform,
    }
    
    return render(request, 'authapp/forgotPassword.html', context)