from ads.models import Category
import pytest


@pytest.mark.django_db
def test_cats_list(client):
    category = Category.objects.create(
        name="Цветы",
        slug=None,
    )

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": category.id,
            "name": "Цветы",
            "slug": None,
        }]
    }

    response = client.get("/cat/")

    assert response.status_code == 200
    assert response.data == expected_response
