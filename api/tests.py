import json

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token

from .models import Application


class AppListViewTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user', password='password')

        Token.objects.create(user=self.test_user)

    def test_create_app(self):

        url = reverse('api:apps')
        request_data = {'ID': 1234, 'name': 'test_app'}

        response = self.client.post(url, data=json.dumps(request_data), content_type="application/json",
                                    HTTP_AUTHORIZATION="Token {}".format(self.test_user.auth_token.key))

        assert response.status_code == 201


class AppViewTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user', password='password')

        Token.objects.create(user=self.test_user)

        self.test_app = Application.objects.create(ID=1234, name='new_app')

    def test_retrieve_app(self):
        url = reverse('api:app', kwargs={'pk': self.test_app.id})

        response = self.client.get(url, HTTP_AUTHORIZATION="Token {}".format(self.test_user.auth_token.key))

        assert response.status_code == 200

    def test_update_app(self):
        url = reverse('api:app', kwargs={'pk': self.test_app.id})
        request_data = {'name': 'TEST_APP'}

        response = self.client.patch(url, data=json.dumps(request_data), content_type="application/json",
                                     HTTP_AUTHORIZATION="Token {}".format(self.test_user.auth_token.key))

        assert response.status_code == 200

    def test_delete_app(self):
        url = reverse('api:app', kwargs={'pk': self.test_app.id})

        response = self.client.delete(url, HTTP_AUTHORIZATION="Token {}".format(self.test_user.auth_token.key))

        assert response.status_code == 204


class AppInfoViewTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user', password='password')

        Token.objects.create(user=self.test_user)

        self.test_app = Application.objects.create(ID=1234, name='new_app')
        self.test_app.create_api_key()

    def test_info_app(self):
        url = reverse('api:app_info', kwargs={'api_key': self.test_app.api_key})

        response = self.client.get(url, HTTP_AUTHORIZATION="Token {}".format(self.test_user.auth_token.key))

        assert response.status_code == 200


class GetUserTokenView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user', password='password')

        Token.objects.create(user=self.test_user)

    def test_get_token(self):
        url = reverse('api:get_user_token')

        request_data = {'username': 'test_user', 'password': 'password'}

        response = self.client.post(url, data=json.dumps(request_data), content_type="application/json")

        assert response.status_code == 200
