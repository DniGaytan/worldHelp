from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.


class Activity(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100)
    activity_description = models.CharField(max_length=700)
    activity_start_date = models.DateField()
    activity_end_date = models.DateField()
    activity_picture = models.FileField()

    EJE_VIDA = 'vida'
    EJE_INNOVACION = 'innovacion'
    EJE_ENERGIA = 'energia'
    EJE_SOCIAL = 'social'

    TIPO_EJES = (
        (EJE_VIDA, 'Vida'),
        (EJE_INNOVACION, 'Innovacion'),
        (EJE_ENERGIA, 'Energia'),
        (EJE_SOCIAL, 'Social')
    )

    activity_type = models.CharField(
        max_length = 10,
        choices = TIPO_EJES,
        default = EJE_VIDA,
    )


    def __str__(self):
        return self.activity_name


class Donation(models.Model):
    MONETARY = 'MTR'
    RESOURCE = 'RSR'
    VOLUNTEER = 'VLT'

    DONATION_TYPES = (
        (MONETARY, 'Monetary'),
        (RESOURCE, 'Resources'),
        (VOLUNTEER, 'Volunteers')
    )

    activity = models.ForeignKey(Activity, default = 1, on_delete=models.CASCADE)
    donation_type = models.CharField(
        max_length = 3,
        choices = DONATION_TYPES,
        default = MONETARY,
    )
    donation_description = models.CharField(max_length = 400)

