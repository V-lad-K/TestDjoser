from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserRegistrationTest(APITestCase):
    def test_user_registration_invalid_username(self):
        url = reverse('user-list')

        data = {
            'username': 'qw',
            'email': 'testuser@example.com',
            'password': 'hgfhJMKKmkmk5675kmk',
            're_password': 'hgfhJMKKmkmk5675kmk'
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
