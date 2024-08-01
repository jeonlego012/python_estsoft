from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.template import TemplateDoesNotExist
from django.http import Http404
from django.contrib import messages

from .forms import UserLoginModelForm, UserRegisterForm, UserChangePasswordForm
from rbacauth.forms import RegistrationForm, LogInForm 

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
        
        # ModelForm 방식
        '''
        userform = UserRegisterModelForm(request.POST)
    
        email = userform.data["email"]
        username = userform.data["username"]
        password = userform.data["password"]
        
        user = User.objects.create_user(email=email, username=username, password=password)
        login(request, user)
        
        return redirect('index:index')
        '''
        
        # Form 방식
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
        context = {}
        
        if self.kwargs["page"] == "login.html":
            # userform = UserLoginModelForm(label_suffix='')
            userform = LogInForm()
            context['userform'] = userform
        elif self.kwargs["page"] == "register.html":
            # userform = UserRegisterForm(label_suffix='')
            userform = RegistrationForm()
            context['userform'] = userform
            
        return context
    
    def post(self, request, page, *args, **kwargs):
        self.template_name = 'authapp/' + page
        context = self.get_context_data(**kwargs)
        
        if page == "login.html":
            # User 방식
            '''
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
            '''
            # CustomUser 방식
            form = LogInForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                try:
                    login(request, user)
                    messages.success(request, f'Welcome {user.username}!')
                    self.success_url = '/index/index.html'
                    return HttpResponseRedirect(self.success_url)
                except:
                    form.add_error('password', form.error_messages)
               
            else:
                form = RegistrationForm()
                messages.error(request, f'{list(form.error_messages.values())[0]}')
            
            return render(request, 'authapp/register.html', {'userform': form})
            
                
        elif page == "register.html":
            # User 방식
            '''
            userform = UserRegisterForm(request.POST)

            email = userform.data["email"]
            username = userform.data["username"]
            password = userform.data["password"]
            password2 = userform.data["password2"]
            is_admin = False
            if 'is_admin' in userform.data.keys():
                is_admin = userform.data["is_admin"]
        
            if password == password2:
                user = User.objects.create_user(email=email, username=username, password=password, is_superuser=is_admin, is_staff=is_admin)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                
                self.success_url = '/index/index.html'
                return HttpResponseRedirect(self.success_url)
            '''
            
            # CustomUser 방식
            form = RegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                
                if password1 == password2:
                    form.save(commit=True)
                    
                    messages.success(request, f'Your account has been created {username}! Proceed to log in')
                    self.success_url = '/authapp/login.html'
                    return HttpResponseRedirect(self.success_url)
                else:
                    form.add_error('password2', 'Passwords entered do not match')
            else:
                form = RegistrationForm()
                messages.error(request, f'{list(form.error_messages.values())[0]}')
            
            return render(request, 'authapp/register.html', {'userform': form})


        try:
            return self.render_to_response(context)
        except TemplateDoesNotExist:
            raise Http404()