from django.urls import path
from Principal import views

urlpatterns =[
    #www.worldhelp.com/
    path('',views.index, name = 'Main')

]