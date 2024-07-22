from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bluemoonapp/index.html')

def dynamic_url(request, url):
    print('result!!!', request, 'url: ' , url)

    url += '.html'

    print(url)

    return render(request, 'bluemoonapp/' + url)