from django.urls import path
from . import views

app_name = "bluemoonapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.upload, name="upload"),
    path("<str:url>/", views.dynamic_index_url),
    path("signup/<str:url>/", views.dynamic_signup_url),
]
