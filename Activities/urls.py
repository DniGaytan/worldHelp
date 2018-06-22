from django.urls import path
from Activities import views

app_name='activities'

urlpatterns = [
   #path('cuando se escriba esto', ejecuta esto)

    #www.worldhelp.com/events
    path('',views.events, name = 'Events'),

    #www.worldhelp.com/events/activity_id
    path('<activity_id>/', views.details, name='Act Details')
]