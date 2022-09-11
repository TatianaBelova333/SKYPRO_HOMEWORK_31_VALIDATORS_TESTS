from pytest_factoryboy import register
from tests.factories import CategoryFactory, AdFactory, UserFactory

pytest_plugins = "tests.fixtures"
register(CategoryFactory)
register(AdFactory)
register(UserFactory)
