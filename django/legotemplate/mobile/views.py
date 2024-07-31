from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist
from django.http import Http404, JsonResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages

import json

from rbacauth.models import CustomUser

# Create your views here.
class StaticView(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = 'mobile/' + page
        response = super(StaticView, self).get(request, page, *args, **kwargs)
        
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()

            
def register(request):
    username = json.loads(request.body)['username']
    email = json.loads(request.body)['email']
    password1 = json.loads(request.body)['password1']
    password2 = json.loads(request.body)['password2']
    
    if password1 == password2:
        try:
            custom_user = CustomUser.objects.get(username=username)
            return JsonResponse({'msg': '이미 가입된 회원입니다'})
        except CustomUser.DoesNotExist:
            custom_user = CustomUser.objects.create_user(username, email, password1)
            
            custom_user.save()
            
            messages.success(request, f'Your account has been created {username} ! Proceed to log in')
            
            msg = "가입 완료!"
            
            return JsonResponse({'msg': msg, 'is_success': True})
    
    else:
        msg = "비밀번호 오류"
            
        return JsonResponse({'msg': msg})
    