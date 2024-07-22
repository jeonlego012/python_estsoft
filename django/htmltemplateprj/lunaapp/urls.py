from django.urls import path
from . import views

app_name = "lunaapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:url>/", views.dynamic_url, name="dynamic_url"),
]
