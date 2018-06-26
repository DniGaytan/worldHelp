from django.shortcuts import render, redirect
from .models import Activity, Donation
from django.http import Http404
from .forms import EventForm
from django.contrib.auth.models import User

# Create your views here.
# {{ display as this variable is in html}}
# {% Use pythone code goes between ths things %}

def events(request):
    # all_acts guarda todas las actividades de la bd
    # return render cargara el archivo html
    # {'all_acts' : all_acts} variable que pasará cosas de la bd al html

    all_acts = Activity.objects.all()
    return render(request, template_name='Activities/Activities_Page.html', context = {'all_acts': all_acts})

def details(request, activity_id):
    try:
        act = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist :
        raise Http404("Activitie does not exist")
    return render(request, template_name='Activities/detail.html', context = {'act': act})

def crear_Evento(request):

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username = request.user.username)
            event = form.save()
            event.user = user
            event.save()
            return redirect(request, reverse('activities:details'), activity_id = Activity.objects.get(activity_name = event.activity_name))
        else:
            context = {
                'form': form
            }
            return render(request, template_name = 'Activities/newEvent.html', context = context )
        
    else:
        context = {
            'form': EventForm(None)
        }

        return render(request, template_name = 'Activities/newEvent.html', context = context )



