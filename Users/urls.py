from django.urls import path
from Users import views

urlpatterns = [
    #www.worldhelp.com/user
    path('', views.UserPage, name='User')
]