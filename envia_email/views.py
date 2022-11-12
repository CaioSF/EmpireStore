from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail




def envia_email(request):
    return HttpResponse('ola')