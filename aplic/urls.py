from django.urls import path

from .views import index, support, login, register

urlpatterns = [
    path('', index, name='index'),
    path('support/', support, name='support'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),

]
