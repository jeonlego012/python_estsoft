from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def index(request):
    tup = (1, 2, 3, 4)
    v = [100]
    now = timezone.now
    member_list = [
        Member('Lego', '010-1111-1111'),
        Member('John', '010-2222-2222'),
        Member('Anna', '010-3333-3333'),
        Member('Joy', '010-4444-4444'),
    ]
    context = {
        'txt': 'test',
        'txt1': tup,
        'txt2': v,
        'txt3': now,
        'txt4': '',
        'txt5': '안녕하십니까불이 장고 테스트중입니다람쥐',
        'txt6': '<open><br>',
        'txt7': '<script>alert("test");</script>',
        'member_list': member_list,
    }
    return render(request, 'index.html', context)

class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f'Member[name={self.name}, phone={self.phone}]'

def get1(request):
    print(request.GET)
    print(request.GET.keys())
    
    keys= request.GET.keys()
    for key in keys:
        val = request.GET[key]
        print(key, val)
    return HttpResponse("get1")

def get2(request, v1, v2, v3):
    print(f'{v1} {v2} {v3}')
    return HttpResponse("get2")

def post1(request):
    print(request.POST)
    print(request.POST.keys())
    
    keys= request.POST.keys()
    for key in keys:
        val = request.POST[key]
        print(key, val)
    return HttpResponse("post1")
    
def post2(request, msg, opt):
    print(request.POST)
    print(request.POST.keys())
    
    keys= request.POST.keys()
    for key in keys:
        val = request.POST[key]
        print(key, val)
    return HttpResponse("post2")

from django.views.generic import View

class TestGet3(View):
    def get(self, request): # 내장 method
        print(request.GET)
        print(request.GET.keys())
    
        keys= request.GET.keys()
        for key in keys:
            val = request.GET[key]
            print(key, val)
        return HttpResponse("TestGet3")

class TestGet4(View):
    def get(self, request, v1, v2, v3):
        print(f'{v1} {v2} {v3}')
        return HttpResponse("TestGet4")
    
class TestPost3(View):
    def post(self, request): # 내장 method
        print(request.POST)
        print(request.POST.keys())
        
        keys= request.POST.keys()
        for key in keys:
            val = request.POST[key]
            print(key, val)
        return HttpResponse("TestPost3")
    
class TestPost4(View):
    def post(self, request, msg, opt):
        print(request.POST)
        print(request.POST.keys())
        
        keys= request.POST.keys()
        for key in keys:
            val = request.POST[key]
            print(key, val)
        return HttpResponse("TestPost4")

class TestGetPost1(View):
     def get(self, request):
        print(request.GET)
        print(request.GET.keys())
    
        keys= request.GET.keys()
        for key in keys:
            val = request.GET[key]
            print(key, val)
        return HttpResponse("TestGetPost1")
    
     def post(self, request):
        print(request.POST)
        print(request.POST.keys())
        
        keys= request.POST.keys()
        for key in keys:
            val = request.POST[key]
            print(key, val)
        return HttpResponse("TestGetPost1")

class TestGetPost2(View):
    def get(self, request, v1, v2, v3):
        print(f'{v1} {v2} {v3}')
        return HttpResponse("TestGetPost2")
    
    def post(self, request, msg, opt):
        print(request.POST)
        print(request.POST.keys())
        
        keys= request.POST.keys()
        for key in keys:
            val = request.POST[key]
            print(key, val)
        return HttpResponse("TestGetPost2")