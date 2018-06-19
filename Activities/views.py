from django.shortcuts import render
from .models import Activity, Donation
from django.http import Http404

# Create your views here.
# {{ display as this variable is in html}}
# {% Use pythone code goes between ths things %}

def events(request):
    # all_acts guarda todas las actividades de la bd
    # return render cargara el archivo html
    # {'all_acts' : all_acts} variable que pasará cosas de la bd al html

    all_acts = Activity.objects.all()
    return render(request, 'Activities/Activities_Page.html', {'all_acts': all_acts})

def details(request, activity_id):
    try:
        act = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist :
        raise Http404("Activitie does not exist")
    return render(request, 'Activities/detail.html', {'act': act})
