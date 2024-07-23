from django.urls import path
from . import views

app_name='boardapp'

urlpatterns = [
    path('', views.index, name='index'),
    
    # function-based
    # path('list/', views.list, name='list'),
    # path('create/', views.create, name='create'),

    # class-based
    path('list/', views.BoardListView.as_view(), name='list'),
    path('list/<int:id>/', views.BoardDetailView.as_view(), name='detail'),
    path('create/', views.BoardCreateView.as_view(), name='create'),
    path('list/<int:id>/update/', views.BoardUpdateView.as_view(), name='update'),
    path('list/<int:id>/delete/', views.BoardDeleteView.as_view(), name='delete'),
]
