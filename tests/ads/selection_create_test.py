import pytest


@pytest.mark.django_db
def test_create_selection(client, user_id_token, ad):
    user_id, user_token = user_id_token
    expected_response = {
        "id": 1,
        "name": "My Selection",
        "owner": user_id,
        "ads": [ad.id],
    }
    data = {
        "name": "My Selection",
        "owner": user_id,
        "ads": [ad.id],
    }

    response = client.post(
        "/selection/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response



