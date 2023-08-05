from django.test import TestCase
from django.urls.base import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'nisan3',
        'email': 'nisan3@test.com',
        'password1': 'kiril111.',
        'password2': 'kiril111.',
    }

    def test_sign_up__when_valid_data__expect_status_code_302(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA
        )
        self.assertEqual(302, response.status_code)

    def test_sign_up__when_valid_data__expect_user_created(self):
        self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA
        )

        searched_user = UserModel.objects.get()
        self.assertIsNotNone(searched_user)

    def test_sign_up__when_valid_data__expect_user_created_username(self):
        self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA
        )

        searched_user_username = UserModel.objects.get().username
        self.assertEqual(self.VALID_USER_DATA['username'], searched_user_username)

    def test_sign_up__when_valid_data__expect_user_created_email(self):
        self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA
        )

        searched_user_email = UserModel.objects.get().email
        self.assertEqual(self.VALID_USER_DATA['email'], searched_user_email)


