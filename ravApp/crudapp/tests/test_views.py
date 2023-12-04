from rest_framework import status

from fixtures.user import user
from fixtures.item import item


class TestItemsView:
    endpoint = '/api/items/'

    def test_list(self, client, user, item):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        items = response.json()
        for _item in items:
            _item['id'] == item.id
            _item['name'] == item.name
            _item['description'] == item.description

    def test_retrieve(self, client, user, item):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(item.id) + "/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == item.id
        assert response.data['name'] == item.name
        assert response.data['description'] == item.description

    def test_create(self, client, user):
        client.force_authenticate(user=user)
        data = {
            "name": "Test Item Name",
            "description": "Test Item Description",
        }
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == data['name']
        assert response.data['description'] == data['description']

    def test_update(self, client, user, item):
        client.force_authenticate(user=user)
        data = {
            "name": "Test Updated Item Name",
            "description": "Test Updated Item Description",
        }
        response = client.put(self.endpoint + str(item.id) + "/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == data['name']
        assert response.data['description'] == data['description']

    def test_delete(self, client, user, item):
        client.force_authenticate(user=user)
        response = client.delete(self.endpoint + str(item.id) + "/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_list_anonymous(self, client):
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_retrieve_anonymous(self, client, item):
        response = client.get(self.endpoint + str(item.id) + "/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_anonymous(self, client):
        data = {"username": "Test Post Body", "password": "test_user"}
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_anonymous(self, client, item):
        data = {
            "name": "Test Updated Item Name",
            "description": "Test Updated Item Description"
        }
        response = client.put(self.endpoint + str(item.id) + "/", data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_anonymous(self, client, item):
        response = client.delete(self.endpoint + str(item.id) + "/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
