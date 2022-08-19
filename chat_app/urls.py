from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat'),
    path('user/<str:params>/', views.chat_user, name='chat-user'),
    path('room/<str:params>/', views.chat_room, name='chat-room')
]