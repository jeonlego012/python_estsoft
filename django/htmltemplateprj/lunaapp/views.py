from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'lunaapp/index.html')
    # return HttpResponse("hi luna")
    
def dynamic_url(request, url):
    print('result!!!', request, 'url: ' , url)

    url += ".html"
    return render(request, "lunaapp/"+url)