from django.urls import path, re_path
from . import views

app_name = "mobile"

urlpatterns = [
    path('register/', views.register, name="register"),
    re_path(r'^(?P<page>.+\.html)$', views.StaticView.as_view()),
    
]