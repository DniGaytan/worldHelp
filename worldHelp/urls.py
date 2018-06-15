from django.contrib import admin
from django.urls import path, include
from Activities import urls as ActUrls
from Users import urls as UserUrls
from . import views

#Cuando el usuario pida alguna pagina, ven aqui.

urlpatterns = [
   #Path('cuando el usuario escriba esto', ven aqui)

    #www.worldhelp.com/admin/
    path('admin/', admin.site.urls),

    #www.worldhelp.com/
    path('', views.index, name = 'Main'),

    #www.worldhelp.com/events
    path('activities/',include(ActUrls)),

    #www.worldhelp.com/user/
    path('user/',include(UserUrls))

]
