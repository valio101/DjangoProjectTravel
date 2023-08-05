from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from djangoProjectTravel.destination.models import Destination
from djangoProjectTravel.photos.models import Photo

UserModel = get_user_model()


def create_destinations_for_user(user, count=5):
    result = []
    for i in range(count):
        destination = Destination(
            destination_name=f'Destination {i + 1}',
            destination_photo=f'http://destinations.com/{i + 1}.jpg',
            information=f'Info {i + 1}',
            user=user,
        )
        destination.save()
        result.append(destination)
    return result


class DetailsPhotoViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'nisan3',
        'email': 'nisan3@test.com',
        'password': 'kiril111.',
    }

    VALID_USER_DATA2 = {
        'username': 'kia3',
        'email': 'kia3@test.com',
        'password': 'kiril111.',
    }

    def _create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        destinations = create_destinations_for_user(user, count=5)
        photo = Photo.objects.create(photo=f'/var/images/img1.png', user=user, destination=destinations[0], )
        response = self.client.get(reverse_lazy('details photo', kwargs={'pk': photo.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        second_user = UserModel.objects.create_user(self.VALID_USER_DATA2)
        destinations = create_destinations_for_user(user, count=5)
        photo = Photo.objects.create(photo=f'/var/images/img1.png', user=second_user, destination=destinations[0], )
        response = self.client.get(reverse_lazy('details photo', kwargs={'pk': photo.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_photo_user_username__when_correct_username(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        destinations = create_destinations_for_user(user, count=5)
        photo = Photo.objects.create(photo=f'/var/images/img1.png', user=user, destination=destinations[0], )
        response = self.client.get(reverse_lazy('details photo', kwargs={'pk': photo.pk}))

        self.assertEqual('nisan3', response.context['photo'].user.username)

    def test_photo_user_username__when_wrong_username(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        destinations = create_destinations_for_user(user, count=5)
        photo = Photo.objects.create(photo=f'/var/images/img1.png', user=user, destination=destinations[0], )
        response = self.client.get(reverse_lazy('details photo', kwargs={'pk': photo.pk}))

        self.assertNotEqual('random', response.context['photo'].user.username)
