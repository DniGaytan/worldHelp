from django.shortcuts import render, redirect
from .models import Activity, Donation
from django.http import Http404
from .forms import EventForm, DonationForm
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
    context = {
        'act': act,
        'donations': Donation.objects.filter(activity = Activity.objects.get(pk=activity_id))
    }
    return render(request, template_name='Activities/detail.html', context = context) 

def crear_evento(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                user = User.objects.get(pk=request.user.id)
                event = form.save()
                event.user = user
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

def crear_donacion(request, activity_id):
    if request.user.is_authenticated :
        if request.method == 'POST':
            form = DonationForm(request.POST)
            if form.is_valid():
                activity = Activity.objects.get(pk=activity_id)
                donation = form.save()
                donation.activity = activity
                donation.save()
                return redirect(reverse('activities:actDetails', kwargs = {'activity_id': activity_id}))
            else:
                context = {
                    'form': DonationForm,
                    'errorList': form.errors,
                    'activity_id': activity_id
                }
                return render(request, template_name="Activities/newDonation.html", context = context)
        else:
            context = {
                'form': DonationForm(None),
                'activity_id': activity_id
            }
            return render(request, template_name="Activities/newDonation.html", context = context)
    else:
        raise Http404('Prohibido pasar')

