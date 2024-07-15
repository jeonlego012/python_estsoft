from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    # 함수 기반 호출 function based
    path('', views.index),
    path('get1/', views.get1, name='get1'),
    path('get2/<int:v1>/<int:v2>/<str:v3>/', views.get2),
    path('post1/', views.post1),
    path('post2/<str:msg>/<str:opt>/', views.post2),
    
    # 클래스 기반 호출 class based
    path('get3/', views.TestGet3.as_view()),
    path('get4/<int:v1>/<int:v2>/<str:v3>/', views.TestGet4.as_view()),
    path('post3/', views.TestPost3.as_view()),
    path('post4/<str:msg>/<str:opt>/', views.TestPost4.as_view()),
    
    
    # Class based
    path('getpost1/get5/', views.TestGetPost1.as_view()),
    path('getpost1/post5/', views.TestGetPost1.as_view()),
    path('getpost2/get6/<int:v1>/<int:v2>/<str:v3>/', views.TestGetPost2.as_view()),
    path('getpost2/post6/<str:msg>/<str:opt>/', views.TestGetPost2.as_view()),
]
