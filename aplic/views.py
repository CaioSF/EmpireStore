from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    return render(request, "index.html", context)

def support(request):
    context = {
        "title": "Página suporte",
        "content": "Bem-vindo a página suporte"
    }
    return render(request, "support.html", context)

def login(request):
    context = {
        "title": "Página de login",
        "content": "Bem-vindo a página de login"
    }
    return render(request, "auth/login.html", context)

def register(request):
    context = {
        "title": "Página de cadastro",
        "content": "Bem-vindo a página de cadastro"
    }
    return render(request, "auth/register.html", context)