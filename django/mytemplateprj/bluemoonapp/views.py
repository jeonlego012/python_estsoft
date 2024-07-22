from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FileUploadForm
from .models import UploadFile

# Create your views here.
def index(request):
    print(f"result!!!!!!! index view in {request.method}")
    return render(request, "bluemoonapp/index.html")

def dynamic_index_url(request, url):
    print(f"result!!!!!!! dynamic index url view in {url} and {request.method}")

    if request.method == "POST":
        if url == "login":
            print(f"result!!! {request.POST['username']} {request.POST['password']}")
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('bluemoonapp:index')
        elif url == "logout":
            logout(request)
            return redirect('bluemoonapp:login')

    url = "bluemoonapp/" + url + ".html"
    

    return render(request, url)

def dynamic_signup_url(request, url):
    print(f"result!!!!!!! dynamic signup url view in {url} and {request.method}")
    url = "bluemoonapp/" + url + ".html"

    return render(request, url)

def upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        
        form.save()
    else:
        form = FileUploadForm()
    return render(request, "bluemoonapp/upload.html", {"form": form})