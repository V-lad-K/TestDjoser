from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserRegistrationTest(APITestCase):
    def test_user_registration_invalid_username_too_short(self):
        url = reverse('user-list')

        data = {
            'username': 'qw',
            'email': 'testuser@example.com',
            'password': 'hgfhJMKKmkmk5675kmk',
            're_password': 'hgfhJMKKmkmk5675kmk'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(str(response.data['username'][0]), 'Username must be in range 5 - 150')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_user_registration_invalid_username_with_space(self):
        url = reverse('user-list')

        data = {
            'username': 'invalid username',
            'email': 'testuser@example.com',
            'password': 'hgfhJMKKmkmk5675kmk',
            're_password': 'hgfhJMKKmkmk5675kmk'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertEqual(str(response.data['username'][0]), 'Username must not contain spaces')

    def test_user_registration_invalid_username_only_numbers(self):
        url = reverse('user-list')

        data = {
            'username': '123456',
            'email': 'testuser@example.com',
            'password': 'hgfhJMKKmkmk5675kmk',
            're_password': 'hgfhJMKKmkmk5675kmk'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertEqual(str(response.data['username'][0]), 'Username should not contain only numbers')

    def test_user_registration_invalid_email_format(self):
        url = reverse('user-list')

        data = {
            'username': 'validusername',
            'email': 'invalid-email',
            'password': 'hgfhJMKKmkmk5675kmk',
            're_password': 'hgfhJMKKmkmk5675kmk'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertEqual(str(response.data['email'][0]), 'Email should contain only latin letters, numbers, underscores, periods, or dashes and must follow the correct format')

    def test_user_registration_invalid_password_too_short(self):
        url = reverse('user-list')

        data = {
            'username': 'validusername',
            'email': 'testuser@example.com',
            'password': 'short1',
            're_password': 'short1'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertEqual(str(response.data['password'][0]), 'Password must be in range 8 - 150')

    def test_user_registration_invalid_password_no_uppercase(self):
        url = reverse('user-list')

        data = {
            'username': 'validusername',
            'email': 'testuser@example.com',
            'password': 'lowercase1234',
            're_password': 'lowercase1234'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertEqual(str(response.data['password'][0]), 'Password must have at least 1 upper character')

    def test_user_registration_invalid_password_no_digit(self):
        url = reverse('user-list')

        data = {
            'username': 'validusername',
            'email': 'testuser@example.com',
            'password': 'NoDigitsPassword',
            're_password': 'NoDigitsPassword'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertEqual(str(response.data['password'][0]), 'Password must have at least 1 digit')

    def test_user_registration_invalid_password_contains_cyrillic(self):
        url = reverse('user-list')

        data = {
            'username': 'validusername',
            'email': 'testuser@example.com',
            'password': 'ValidPass123Пароль',
            're_password': 'ValidPass123Пароль'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertEqual(str(response.data['password'][0]), 'The password must not contain Cyrillic characters')
