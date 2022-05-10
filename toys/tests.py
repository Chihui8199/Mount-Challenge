from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


# TODO: Use faker to generate data automatically
class ToyViewSetAPIViewTests(APITestCase):
    toys_url = reverse('toy-list')
    toy_detail_url = reverse('toy-detail', args=['Toy2'])

    # Setup run before every test method.
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz'
        )
        self.client.force_login(user=self.user)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        # saving data to populate test database
        data = {
            "toy_item": "Toy2",
            "price": "4.10"
        }
        self.client.post(self.toys_url, data, format='json')

    def test_get_toy_list_authenticated(self):
        response = self.client.get(self.toys_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_toy_list_unauthenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.toys_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_toy_details_authenticated(self):
        response = self.client.get(self.toy_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['toy_item'], 'Toy2')

    def test_get_toy_details_unauthenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.toy_detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_toy_detail_authenticated(self):
        data = {
            "toy_item": "Toy3",
            "price": "1.00"
        }
        response = self.client.post(self.toys_url, data, format='json')
        self.assertEqual(response.data['toy_item'], "Toy3")
        self.assertEqual(response.data['price'], "1.00")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_toy_detail_unauthenticated(self):
        data = {
            "toy_item": "Toy3",
            "price": "1.00"
        }
        self.client.force_authenticate(user=None, token=None)
        response = self.client.post(self.toys_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_toy_detail_unauthenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.delete(self.toy_detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_toy_detail_authenticated(self):
        response = self.client.delete(self.toy_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Clean up run after every test method.
    def tearDown(self):
        return super().tearDown()
