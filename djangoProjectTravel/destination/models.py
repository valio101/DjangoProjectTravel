from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Destination(models.Model):
    MAX_NAME = 30
    destination_name = models.CharField(max_length=MAX_NAME, null=False, blank=False, )
    destination_photo = models.URLField(null=False, blank=False, )
    information = models.TextField(null=True, blank=True)
    recommendation_to_visit = models.BooleanField(default=True)

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, )

    def __str__(self):
        return f'{self.destination_name}'
