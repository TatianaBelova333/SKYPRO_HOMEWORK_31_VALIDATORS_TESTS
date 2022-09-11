import factory

from ads.models import Category, Ad
from authentication.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Pets"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    role = 'member'
    first_name = "Vasily"
    last_name = "Ivanov"
    username = factory.Faker("name")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Cell phone"
    author = factory.SubFactory(UserFactory)
    price = 500
    description = "New iPhone 14"
    is_published = False
    image = None
    category = factory.SubFactory(CategoryFactory)

