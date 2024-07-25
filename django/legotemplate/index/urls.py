from django.urls import path, re_path
from . import views

app_name = "index"

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^(?P<page>.+\.html)$', views.StaticView.as_view()),
    path('email_send/', views.send_email, name='send_email'),
]