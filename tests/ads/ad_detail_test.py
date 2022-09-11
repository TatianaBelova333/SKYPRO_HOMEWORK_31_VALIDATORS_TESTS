import pytest


@pytest.mark.django_db
def test_ad_detail(client, user_id_token, ad):
    _, user_token = user_id_token
    expected_response = {
        "author": {
            "id": ad.author.pk,
            "first_name": ad.author.first_name,
            "last_name": ad.author.last_name,
        },
        "id": ad.pk,
        "is_published": ad.is_published,
        "name": ad.name,
        "price": ad.price,
        "description": ad.description,
        "image": None,
        "category": ad.category.name,
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
