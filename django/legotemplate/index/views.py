from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method == "POST":
        # logout
        logout(request)
        return redirect('index:index')
    
    return render(request, 'index/index.html')