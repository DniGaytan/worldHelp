from django.urls import path
from Activities import views

app_name='activities'

urlpatterns = [
   #path('cuando se escriba esto', ejecuta esto)
    path('',views.events, name = 'Events'),
    path('details/<activity_id>/', views.details, name='actDetails'),
    path('nuevo/', views.crear_evento, name='newEvent'),
    path('nuevo/<activity_id>/donacion', views.crear_donacion, name="newDonation"),
    path('contribuir/<donation_id>/', views.contribuir, name="contribution")

]