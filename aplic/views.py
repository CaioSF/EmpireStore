from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm

from .models import Produto

class ProdutoListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada
    queryset = Produto.objects.all()






User = get_user_model()

def index(request):
    context = {
                    "title": "Home Page",
                    "content": "Bem vindo a Home Page",
              }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "index.html", context) 

class SuporteView(TemplateView):
    template_name = 'suporte.html'

class PedidosView(TemplateView):
    template_name = 'pedidos.html'




def entrar(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            # redireciona para uma pagina de sucesso
            return redirect("/")
        else:
            #retorna uma mensagem de erro
            print("Login inválido")
    return render(request, "auth/entrar.html", context)
    

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        print('create new cart')
        request.session['cart_id'] = 12
    else:
        print("Cart ID exists")
    return render(request, "carts/home.html", {})


def cadastro(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/cadastro.html", context)