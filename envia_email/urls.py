from django.urls import path
from . import views



urlpatterns = [
    path('email/', views.envia_email, name='envia_email'),
]
