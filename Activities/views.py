from django.shortcuts import render, redirect
from .models import Activity, Donation
from django.http import Http404
from .forms import EventForm, DonationForm, ContributionForm
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.core.mail import send_mail

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

    print(request.user)
    print(Activity.objects.get(pk=activity_id).user)

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
    activity = Activity.objects.get(pk=activity_id)
    if request.user.is_authenticated and activity.user == request.user:
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
        if not request.user.is_authenticated:
            raise Http404('No has iniciado sesion')
        elif(activity.user is not request.user):
            raise Http404('Tu no eres el propietario de esta actividad')
        else:
            raise Http404('Algo raro paso. Si crees que esto es un error reportalo al administrador del sitio')

def contribuir(request, donation_id):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContributionForm(request.POST)
            if form.is_valid():
                send_mail(
                    subject = Donation.objects.get(pk=donation_id).donation_type,
                    message = form.cleaned_data['message'] + "\n" + "de: "+ form.cleaned_data['name'] + "\n" + "tel: " + form.cleaned_data['phoneNumber'],
                    from_email = form.cleaned_data['sender'],
                    recipient_list = [Activity.objects.get(pk=Donation.objects.get(pk=donation_id).activity.id).user.email],
                    fail_silently = False
                )

                return redirect(reverse('activities:actDetails', kwargs={'activity_id': Donation.objects.get(pk=donation_id).activity.id }))
            else:
                context = {
                'form': ContributionForm,
                'donation_id': donation_id
                }

                return render(request, template_name='Activities/contribution.html', context = context)

        else:
            context = {
                'form': ContributionForm(None),
                'donation_id': donation_id
            }

            return render(request, template_name='Activities/contribution.html', context = context)
    else:

        return redirect(reverse('principal:Main'))

