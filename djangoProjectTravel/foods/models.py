from django.db import models
from django.contrib.auth import get_user_model

from djangoProjectTravel.destination.models import Destination

UserModel = get_user_model()


class Food(models.Model):
    MAX_NAME = 30
    food_name = models.CharField(max_length=MAX_NAME, null=False, blank=False, )
    food_photo = models.URLField(null=False, blank=False, )
    opinion = models.TextField(null=True, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.RESTRICT, )
    publication_date = models.DateField(auto_now=True, null=False, blank=False, )

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, )

