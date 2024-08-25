import pytest

from asso.models import Association, Image
from asso.tests.factories import AssociationFactory, ImageFactory
from . import views

@pytest.mark.django_db
def test_association_photos_view():
    """Test the association photos view."""
    association = AssociationFactory()
    image = ImageFactory(asso=association)

    request = pytest.helpers.create_request(
        user=association.manager.user
    )
    response = views.association_photos(request, association.id)
    assert response.status_code == 200

    request = pytest.helpers.create_request(
        user=pytest.helpers.create_user()
    )
    response = views.association_photos(request, association.id)
    assert response.status_code == 404

    request = pytest.helpers.create_request(
        user=association.manager.user
    )
    response = views.association_photos(request, association.id)
    assert response.status_code == 200

    request = pytest.helpers.create_request(
        user=association.manager.user
    )
    response = views.association_photos(request, association.id)
    assert response.status_code == 200
