from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from djangoProjectTravel.destination.models import Destination
from djangoProjectTravel.photos.validators import validate_image_less_than_5mb

UserModel = get_user_model()


class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        return ', '.join(f'{str_field}={self.__dict__[str_field]}' for str_field in self.str_fields)


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('photo',)
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    # photo = models.ImageField(null=False, blank=True, )
    photo = models.ImageField(upload_to='destination_photos/', validators=(validate_image_less_than_5mb,), )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    publication_date = models.DateField(auto_now=True, null=False, blank=False, )

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, )

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, )

