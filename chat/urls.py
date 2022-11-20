from django.urls import path
from . import views

urlpatterns = [
    path('chat_home/', views.home, name='chat_home'),
    path('<str:room>/', views.room, name='room'),
    path('chat_home/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]