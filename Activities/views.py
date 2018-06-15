from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity, Donation
from django.template import loader
# Create your views here.
# {{ display as this variable is in html}}
# {% Use pythone cothe goes between ths things %}

def events(request):
    # all_acts guarda todas las actividades de la bd
    # template cargara el archivo html
    # Context variable que pasará cosas de la bd al html
    all_acts = Activity.objects.all()

    template = loader.get_template('Activities/Activities_Page.html')

    context = {
        'all_acts' : all_acts
    }
    return HttpResponse(template.render(context, request))

def details(request, activity_id):
    return HttpResponse("<h2> Details de la actividad con ID: " + str(activity_id) + "</h2>")
