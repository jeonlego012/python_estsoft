from django.urls import path, re_path
from . import views

app_name = "authapp"

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('change_password/', views.changePassword, name="change_password"),
    # class-based
    re_path(r'^(?P<page>.+\.html)$', views.StaticView.as_view()),
]