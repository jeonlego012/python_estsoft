from django.urls import path
from . import views

app_name = "htmltemplateapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.view_login, name="login"),
    path("logout/", views.view_logout, name="logout"),
    path("register/", views.register, name="register"),
    
]
