""" Factories class """
# pylint: disable=too-few-public-methods
from django.contrib.auth import get_user_model

# 3rd Party Libraries
import factory
from factory import Faker
from factory.declarations import SubFactory

class UserFactory(factory.django.DjangoModelFactory):
    """ User factory class """
    class Meta:
        """ Class Meta """
        model = get_user_model()
        django_get_or_create = ["username"]

    username = Faker("user_name")
    email = Faker("email")
    is_active = Faker("boolean")
    is_staff = Faker("boolean")
    password = factory.PostGenerationMethodCall("set_password", "password")

class CategoryFactory(factory.django.DjangoModelFactory):
    """ Category factory class"""
    class Meta:
        """ Class Meta """
        model = "api.Category"

    name = Faker("name")
    slug = Faker("name")

class SectionFactory(factory.django.DjangoModelFactory):
    """ Section factory class """
    class Meta:
        """ Meta class """
        model = "api.Section"

    name = Faker("name")
    rank = Faker("name")

class EventFactory(factory.django.DjangoModelFactory):
    """ Event factory class """
    class Meta:
        """ Meta class """
        model = "api.Event"

    name = Faker("name")
    category = SubFactory(CategoryFactory)

class SeatFactory(factory.django.DjangoModelFactory):
    """ Seat factory class """
    class Meta:
        """ Meta class """
        model = "api.Seat"

    seat_no = Faker("pyint", max_value=10 ** 9)
    row_no = Faker("pyint", max_value=10 ** 9)
    column_no = Faker("pyint", max_value=10 ** 9)
    section = SubFactory(SectionFactory)
    property = Faker("name")
    _isEmpty = Faker("boolean")
    event_no = SubFactory(EventFactory)
