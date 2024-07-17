from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('', views.index),
    path('list/', views.list, name='list'),
    path('form/', views.form, name='form'),
]
