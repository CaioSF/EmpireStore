from django.shortcuts import render

def cart_home(request):
    request.session['first_name'] = 'Pedro'
    return render(request, "carts/home.html", {} )