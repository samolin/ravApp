import pytest

from fixtures.user import user
from crudapp.models import Item


@pytest.fixture
def item(db, user):
    return Item.objects.create(name="Item number 1", description="Description number 1")
