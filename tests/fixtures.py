import pytest


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def user_id_token(client, django_user_model):
    username = 'vova'
    password = "123qwe"

    user = django_user_model.objects.create_user(
        username=username,
        password=password,
        role="member"
    )
    response = client.post(
        "/user/login/",
        {"username": username, "password": password},
        formart='json'
    )

    return user.id, response.data["token"]
