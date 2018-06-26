from django.shortcuts import render, redirect
from .models import Activity, Donation
from django.http import Http404
from .forms import EventForm
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

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
        raise Http404("Activity does not exist")
    return render(request, template_name='Activities/detail.html', context = {'act': act})

def crear_Evento(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                form.user = User.objects.get(username = request.user.username)
                event = form.save()
                event.save()
                return redirect(reverse('activities:actDetails', kwargs = {'activity_id': event.id}))
            else:
                context = {
                    'form': EventForm(None),
                    'errorList': form.errors
                }

                print(form.errors)

                return render(request, template_name= "Activities/newEvent.html", context = context)
        else:
            context = {
                'form': EventForm(None)
            }

            return render(request, template_name="Activities/newEvent.html", context = context)
    else:
        raise Http404



