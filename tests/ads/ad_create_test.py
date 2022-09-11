import pytest


@pytest.mark.django_db
def test_create_ad(client, user_id_token, category):
    user_id, user_token = user_id_token
    expected_response = {
        "author": user_id,
        "id": 1,
        "is_published": False,
        "name": "Старая книга",
        "price": 750,
        "description": "Твердый переплет, состояние прекрасное.",
        "image": None,
        "category": category.pk,
    }

    data = {
        "author": user_id,
        "is_published": False,
        "name": "Старая книга",
        "price": 750,
        "description": "Твердый переплет, состояние прекрасное.",
        "image": None,
        "category": category.pk,
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_incorrect_published_status(client, user_id_token, category):
    user_id, user_token = user_id_token

    data = {
        "author": user_id,
        "is_published": True,
        "name": "Старая книга",
        "price": 750,
        "description": "Твердый переплет, состояние прекрасное.",
        "image": None,
        "category": category.pk,
        }

    expected_response = {
        "is_published": [
            "Incorrect status"
        ]
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 400
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_incorrect_price(client, user_id_token, category):
    user_id, user_token = user_id_token

    data = {
        "author": user_id,
        "is_published": False,
        "name": "Старая книга",
        "price": -750,
        "description": "Твердый переплет, состояние прекрасное.",
        "image": None,
        "category": category.pk,
        }

    expected_response = {
        "price": [
            "Ensure this value is greater than or equal to 0."
        ]
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 400
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_short_name(client, user_id_token, category):
    user_id, user_token = user_id_token

    data = {
        "author": user_id,
        "is_published": False,
        "name": "Книга",
        "price": 750,
        "description": "Твердый переплет, состояние прекрасное.",
        "image": None,
        "category": category.pk,
        }

    expected_response = {
        "name": [
            "Ensure this field has at least 10 characters."
        ]
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 400
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_long_description(client, user_id_token, category):
    user_id, user_token = user_id_token

    data = {
        "author": user_id,
        "is_published": False,
        "name": "Старая Книга",
        "price": 750,
        "description": "Твердый переплет, состояние прекрасное. Есть несколько царапин и пометок. Твердый переплет, "
                       "состояние прекрасное. Есть несколько царапин и пометок. Твердый переплет, состояние "
                       "прекрасное. Есть несколько царапин и пометок. Твердый переплет, состояние прекрасное. Есть "
                       "несколько царапин и пометок. Твердый переплет",
        "image": None,
        "category": category.pk,
        }

    expected_response = {
        "description": [
             "Ensure this field has no more than 300 characters."
        ]
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 400
    assert response.data == expected_response
