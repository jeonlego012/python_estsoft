from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the main index.")
    return render(request, 'templates/main/test.html')

def test(request):
    s = "<html><h1>test</h1></html>"
    return HttpResponse(s)
