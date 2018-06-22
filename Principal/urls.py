from django.urls import path
from Principal import views

app_name="principal"

urlpatterns =[
    #www.worldhelp.com/
    path('',views.index, name = 'Main')

]