from django.shortcuts import render
from Activities.models import Activity
# Create your views here.
# {{ display as this variable is in html}}
# {% Use pythone code goes between ths things %}

def index(request):
    # return render cargara el archivo html

    context = {
    	"eventos": Activity.objects.all()
    }

    return render(request, 'Principal/Main.html', context)