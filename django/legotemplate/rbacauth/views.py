from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 == password2:
                user.set_password(password1)
                user.save()
                
                messages.success(request, f'Your account has been created {username}! Proceed to log in')
                return redirect('authapp/login.html')
            else:
                form.add_error('password2', 'Passwords entered do not match')
    else:
        form = RegistrationForm()
    
    return render(request, 'authapp/register.html', {'userform': form})
