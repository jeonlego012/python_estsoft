from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    res = render(request, 'authapp/index.html')
    
    # cookie
    # print(request.COOKIES)
    # cookie_name = 'django_cookie_name'
    # cookie_value = 'django_cookie_value 5678'
    # res.set_cookie(cookie_name, cookie_value)
    
    # session
    print(request.session)
    
    return res

def signin(request):
    if request.method == "GET":
        if 'username' in request.COOKIES.keys():
            context = {
                'username': request.COOKIES['username'],
            }
            return render(request, 'signin.html', context)
        else:
            return render(request, 'signin.html')
        
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        # https://docs.djangoproject.com/en/5.0/topics/auth/default/#authenticating-users
        user = authenticate(username=username, password=password)
        
        if user is not None :
            redi = redirect('authapp:index')
            # cookie
            redi.set_cookie('username', user.username, max_age=30)
            
            # https://docs.djangoproject.com/en/5.0/topics/auth/default/#how-to-log-a-user-in
            login(request, user)
            
            # session
            request.session['login_user'] = username
            request.session.set_expiry(30)
            return redi
            
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
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        
        return redirect('authapp:index')
    
def signout(request):
    # logout(request)
    request.session.flush()
    return redirect('authapp:index')