import pytest

from fixtures.user import user
from crudapp.models import Item


@pytest.mark.django_db
def test_create_post(user):
    item = Item.objects.create(name="Item number 1", description="Description number 1")
    assert item.name == "Item number 1"
    assert item.description == "Description number 1"