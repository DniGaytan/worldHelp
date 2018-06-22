from django.urls import path
from Users import views

app_name='users'

urlpatterns = [
    #www.worldhelp.com/user
    path('login/', views.userLogin, name='user_login'),
    path('logout/', views.userLogout, name='user_logout'),
    path('register/', views.userRegister, name='user_register'),
]