from django.shortcuts import render

# Create your views here.
# {{ display as this variable is in html}}
# {% Use pythone code goes between ths things %}

def index(request):
    # return render cargara el archivo html
    return render(request, 'Principal/Main.html')