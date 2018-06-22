from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from .forms import UserForm
from django.http import HttpResponse



# Create your views here.

def userRegister(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return #Aqui va la pagina de inicio

    context = {
        "form": form,
    }

    return #Aqui va la pagina de registro

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        passoword = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return #Aqui va la pagina de inicio
        else:
            return #Aqui va la pagina de login con el error de que la cuenta es inexistente, hubo un error en el login o que fue baneada
    return #Aqui va la pagina de login

def userLogout(request):
    logout(request)
    form = UserForm(request.POST or None)
    return #Aqui va la pagina de login, no dejes pasar al usuario a otro lado del sitio hasta que se registre o se loggee
