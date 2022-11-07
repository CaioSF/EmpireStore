from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm

from .models import Produto


class ProdutoFeaturedListView(ListView):
    template_name = "produtos/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Produto.objects.featured()
        

class ProdutoFeaturedDetailView(DetailView):
    queryset = Produto.objects.all().featured()
    template_name = "produtos/featured-detail.html"

    #def get_queryset(self, *args, **kwargs):
        #request = self.request
        #return Product.objects.featured()


class ProdutoListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada
    queryset = Produto.objects.all()
    template_name = "produtos/list.html"

    #def get_context_data(self, *args, **kwargs):
    #    context = super(ProdutoListView, self).get_context_data(*args, **kwargs)
    #    print(context)
    #    return context


class ProdutoDetailView(DetailView):
    template_name = "produtos/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Produto.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance


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