from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import RegistrationCode
from rest_framework import status
from django.contrib.auth.models import User


class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user.
        self.registration_code = RegistrationCode.objects.create(email='nbhlzhou@gmail.com', registration_code='TESTCODE1')
        # self.registration_code = RegistrationCode.objects.create(email='hzhou@blissmotors.com', registration_code='TESTCODE2')
        self.test_user = User.objects.create(username='testuser', email='nbhlzhou@gmail.com', password='testpassword')

        print(User.objects.count())
        # URL for creating an account.
        self.create_url = reverse('user-create')
        # print(self.create_url)

    def test_create_registration_code(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """

        data = {
            'email': 'hzhou@blissmotors.com',
            'registration_code': 'TESTCODE2',
        }

        response = self.client.post(reverse('registration_code-create'), data, format='json')

        print(response)
        # We want to make sure we have two users in the database..
        self.assertEqual(RegistrationCode.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['email'], data['email'])

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """

        self.registration_code = RegistrationCode.objects.create(email='hzhou@blissmotors.com',
                                                                 registration_code='TESTCODE2')

        data = {
            'username': 'foobar',
            'email': 'hzhou@blissmotors.com',
            'password': 'somepassword',
            'registration_code': 'TESTCODE2',
        }

        response = self.client.post(self.create_url, data, format='json')

        print(response)
        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)
