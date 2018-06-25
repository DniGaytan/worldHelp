from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from .forms import UserForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse



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
            return redirect(reverse('principal:Main'))
        else:
            if len(form.cleaned_data['password']) < 8:
                form.add_error('password', 'La contraseña es muy corta')
            if form.errors['username']:
                form.add_error('username', 'Una cuenta ya ha sido registrada con ese usuario')
            if form.errors['email']:
                form.add_error('email', 'Ingresa un correo valido')
                
            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, template_name='Users/register.html', context = context)
    else:
        context = {
            'form': form,
            'errors': None,
        }

        return render(request, template_name='Users/register.html', context = context)

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('principal:Main'))
        else:
            context = {
                'form': UserForm(None),
                'errors': True
            }
            return render(request, template_name = 'Users/login.html', context = context)
    else:
        context = {
            'form': UserForm(None),
            'error': False
        }
        
        return render(request, template_name = 'Users/login.html', context = context)


def userLogout(request):
    logout(request)
    form = UserForm(request.POST or None)
    return #Aqui va la pagina de login, no dejes pasar al usuario a otro lado del sitio hasta que se registre o se loggee
