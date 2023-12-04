import pytest
from rest_framework import status

from fixtures.user import user


class TestAuthenticationViewSet:
    endpoint = '/api/'

    def test_login(self, client, user):
        data = {"username": user.username, "password": "test_password"}
        response = client.post(self.endpoint + "login/", data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']
        assert response.data['refresh']

    @pytest.mark.django_db
    def test_register(self, client):
        data = {
            "username": "johndoe",
            "email": "johndoe@yopmail.com",
            "password": "test_password",
            "first_name": "John",
            "last_name": "Doe",
        }
        response = client.post(self.endpoint + "register/", data)
        assert response.status_code == status.HTTP_201_CREATED
