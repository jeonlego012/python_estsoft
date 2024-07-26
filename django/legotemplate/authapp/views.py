from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.template import TemplateDoesNotExist
from django.http import Http404

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
        
        try:
            user = User.objects.get(email=email)
        except :
            userform = UserChangePasswordForm(label_suffix='')
            context = {
                'userform': userform,
            }
            return render(request, 'authapp/forgotPassword.html', context)
        
        print(f"result!! {email} {password} {password2} {user.username}")
            
        if password == password2:
            user.set_password(password)
            user.save()
            
            return redirect('index:index')
    else:
        userform = UserChangePasswordForm(label_suffix='')
    
    context = {
        'userform': userform,
    }
    
    return render(request, 'authapp/forgotPassword.html', context)

# class-based
class StaticView(FormView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = 'authapp/' + page
        response = super(StaticView, self).get(request, page, *args, **kwargs)
        
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()
        
    def get_context_data(self, **kwargs):
        if self.kwargs["page"] == "login.html":
            userform = UserLoginModelForm(label_suffix='')
        elif self.kwargs["page"] == "register.html":
            userform = UserRegisterForm(label_suffix='')
        context = {
            'userform': userform,
        }
        return context
    
    def post(self, request, page, *args, **kwargs):
        self.template_name = 'authapp/' + page
        context = self.get_context_data(**kwargs)
        
        if page == "login.html":
            userform = UserLoginModelForm(request.POST)
            username = userform.data["username"]
            password = userform.data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                self.success_url = '/index/index.html'
                
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(context) 
                
        elif page == "register.html":
            userform = UserRegisterForm(request.POST)

            email = userform.data["email"]
            username = userform.data["username"]
            password = userform.data["password"]
            password2 = userform.data["password2"]
        
            if password == password2:
                user = User.objects.create_user(email=email, username=username, password=password)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                
                self.success_url = '/index/index.html'
                return HttpResponseRedirect(self.success_url)
            
        
        
        try:
            return self.render_to_response(context)
        except TemplateDoesNotExist:
            raise Http404()