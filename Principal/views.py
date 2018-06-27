from django.shortcuts import render
from Activities.models import Activity
from django.contrib.auth.models import User
# Create your views here.
# {{ display as this variable is in html}}
# {% Use pythone code goes between ths things %}

def index(request):
    # return render cargara el archivo html

    context = {
    	"eventos": Activity.objects.all(),
    	"eventos_vida": Activity.objects.filter(activity_type = "vida")[:4],
    	"eventos_innovacion": Activity.objects.filter(activity_type = "innovacion")[:4],
    	"eventos_energia": Activity.objects.filter(activity_type = "energia")[:4],
    	"eventos_social": Activity.objects.filter(activity_type = "social")[:4],
    }

    return render(request, 'Principal/Main.html', context = context)