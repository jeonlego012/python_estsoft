from django.shortcuts import render

# Create your views here.
# 전체적인 구조를 이해하기 위해 한 파일에 form, model, view 모두 구현
# models.py forms.py가 중요한게 아님.

# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

# forms.py
# https://docs.djangoproject.com/en/5.0/ref/forms/fields/
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        label = '이름',
        max_length = 20,
        required = True
    )
    
    age = forms.IntegerField(
        label = '나이',
        required = True,
    )
    
    email = forms.EmailField(
        label = '이메일',
        required = True,
    )
    
    check = forms.BooleanField(
        label = '아이디 저장',
        required = False,
    )
    


from django.forms import ModelForm, TextInput, NumberInput, EmailInput

class UserModelForm(ModelForm):
    class Meta:
        # 상속받을 모델
        model = User
        
        # 필드 선언
        fields = ['name', 'age', 'email']
        
        # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#built-in-widgets
        widgets = {
            'name': TextInput(
                attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'age': NumberInput(
                attrs={
                'class': "form-control",
                'style': 'max-width: 100px;',
                'placeholder': 'Age'
                }),
            'email': EmailInput(
                attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
        }

# views.py
def index(request):
    if request.method == "POST":
        myuserform = UserForm(request.POST)
        print(myuserform)
        # User.objects.create(myuserform.name, ...)
        # model에 form을 집어넣고 model로 DB에 저장 -> 번거로움 => ModelForm

        usermodelform = UserModelForm(request.POST)
        usermodelform.save()
        
    userform = UserForm() # 소스코드
    # print(userform)
    
    usermodelform = UserModelForm()
    print(usermodelform)
    
    context = {
        'userform': userform,
        'usermodelform': usermodelform,
    }
    return render(request, "formapp/index.html", context)
