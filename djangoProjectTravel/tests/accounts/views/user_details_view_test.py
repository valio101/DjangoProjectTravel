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


class UserDetailsViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'nisan3',
        'email': 'nisan@test.com',
        'password': 'kiril111.',
    }

    def _create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_user_details__when_owner__expect_is_owner_true(self):
        # user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        # self.client.login(**self.VALID_USER_DATA)
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        profile_user = self._create_user_and_login({
            'username': self.VALID_USER_DATA['username'] + '1',
            'email': self.VALID_USER_DATA['email'] + '1',
            'password': self.VALID_USER_DATA['password'],
        })
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': profile_user.pk}))
        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_no_destinations__expect_destinations_count_0(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(0, response.context['destination_count'])

    def test_user_details__when_destinations_and_no_photos__expect_destinations_count_and_photos_count_0(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        destinations = create_destinations_for_user(user, count=5)
        # destination1 = destinations[0]
        # print(destination1)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        # print(response.context['destination_count'])

        self.assertEqual(5, response.context['destination_count'])
        self.assertEqual(0, response.context['photos_count'])

    def test_user_details__when_destinations_and_1_photo__expect_destinations_count_and_photo_count_1(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        destinations = create_destinations_for_user(user, count=5)
        Photo.objects.create(photo=f'/var/images/img1.png', user=user, destination=destinations[0], )

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        # print(response.context['photos'][0])
        self.assertEqual(5, response.context['destination_count'])
        self.assertEqual(1, response.context['photos_count'])

    def test_user_details__when_destinations_and_1_photo__expect_destinations_count_and_photo_count_2(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        destinations = create_destinations_for_user(user, count=5)
        Photo.objects.create(photo=f'/var/images/img1.png', user=user, destination=destinations[0], )
        Photo.objects.create(photo=f'/var/images/img2.png', user=user, destination=destinations[0], )

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        # print(response.context['photos'][0])
        # print(response.context['photos'][1])
        self.assertEqual(5, response.context['destination_count'])
        self.assertEqual(2, response.context['photos_count'])

    def test_user_details__when_destinations_and_4_photos__page_1_photo_count_4(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        destinations = create_destinations_for_user(user, count=5)
        photos = [
            Photo.objects.create(photo=f'/var/images/img1.png', user=user, destination=destinations[0], ),
            Photo.objects.create(photo=f'/var/images/img2.png', user=user, destination=destinations[0], ),
            Photo.objects.create(photo=f'/var/images/img3.png', user=user, destination=destinations[0], ),
            Photo.objects.create(photo=f'/var/images/img4.png', user=user, destination=destinations[0], )
            ]

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}),
                                   data={
                                       'page': 1
                                   })

        self.assertEqual(4, response.context['photos_count'])
        self.assertEqual(photos[0:2], list(response.context['photos']))

    def test_user_details__when_destinations_and_4_photos__page_2_photo_count_4(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        destinations = create_destinations_for_user(user, count=5)
        photos = [
            Photo.objects.create(photo=f'/var/images/img1.png', user=user, destination=destinations[0], ),
            Photo.objects.create(photo=f'/var/images/img2.png', user=user, destination=destinations[0], ),
            Photo.objects.create(photo=f'/var/images/img3.png', user=user, destination=destinations[0], ),
            Photo.objects.create(photo=f'/var/images/img4.png', user=user, destination=destinations[0], )
            ]

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}),
                                   data={
                                       'page': 2
                                   })

        self.assertEqual(4, response.context['photos_count'])
        self.assertEqual(photos[2:4], list(response.context['photos']))

