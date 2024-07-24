from django.urls import path
from . import views

app_name = "authapp"

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('change_password/', views.changePassword, name="change_password"),
]