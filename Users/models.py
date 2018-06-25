from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Saves user extra information that the Model User can't
class User_extra(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	organization = models.BooleanField()
	profile_picture = models.FileField()
