from django.shortcuts import render
from django.db.models import Q
from django.template import loader
from django.http import HttpResponse

from .models import Member

# Create your views here.

def index(request):
    mbr = Member.objects.filter(name__contains='e')
    print(mbr)
    
    # Q : or, and 연산
    mbr = Member.objects.filter(Q(name__contains='l') | Q(name__contains='o'))
    print(mbr)
    
    mbr = Member.objects.all()
    print(mbr)
    
    mbr = Member.objects.all().order_by('age')
    print(mbr)
    
    mbr = Member.objects.all().order_by('name')
    print(mbr)
    

    return render(request, 'index.html')


def list(request):
    members = Member.objects.all().order_by('-id')
    
    context = {
        'members': members,
    }
    
    # 1
    # tpl = loader.get_template('list.html')
    # html = tpl.render(context)
    # return HttpResponse(html)

    # 2
    return render(request, 'list.html', context)


def form(request):
    if request.method == 'POST' :
        return render(request, 'form.html')
    else:
        print(request.method + request.GET['id'])
        member = Member.objects.get(id = request.GET['id'])
        print(member.name)
        context = {
            'id': member.id,
            'name': member.name,
            'age': member.age,
            'explain': member.explain,
        }
        return render(request, 'form.html', context)
    

def save(request):
    value_dict = request.POST
    id = request.GET['id']
    name = value_dict['name']
    age = value_dict['age']
    explain = value_dict['explain']
    
    # 생성
    if id == '':
        member = Member(name=name, age=age, explain=explain)
    # 수정
    else:
        member = Member.objects.get(id=id)
        member.name = name
        member.age = age
        member.explain = explain
        
    
    # Member.objects.create(name=name, age=age, explain=explain)

    member.save()

    return render(request, 'save.html')

