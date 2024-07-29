from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist
from django.http import Http404
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        # logout
        logout(request)
        return redirect('index:index')
    
    return render(request, 'index/index.html')

class StaticView(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = 'index/' + page
        response = super(StaticView, self).get(request ,*args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()
    
    def post(self, request, page, *args, **kwargs):
        logout(request)
        
        self.template_name = 'index/index.html'
        
        context = self.get_context_data(**kwargs)
        
        try:
            return self.render_to_response(context)
        except TemplateDoesNotExist:
            raise Http404()
    

def send_email(request):
    subject = 'test title'
    to = ["jyo9873@gmail.com"]
    message = 'test contents'
    
    EmailMessage(subject=subject, body=message, to=to).send()
    
    return HttpResponse(f'email ok ')