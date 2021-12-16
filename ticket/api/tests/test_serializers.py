""" Test """
# pylint: disable=maybe-no-member
from django.test import TestCase

from api.models import Seat
from api.models import Event
from api.models import Category
from api.models import Section

from api.serializers import SeatSerializer
from api.serializers import EventSerializer
from api.serializers import CategorySerializer
from api.serializers import SectionSerializer
from api.serializers import AllocateSerializer

class SerializersTests(TestCase):
    """ Serializers tests """
    def setUp(self):
        """ Set up """
        Category.objects.create(
            name='First',
            slug='first'
        )

        Section.objects.create(
            name='High',
            rank='1st'
        )

        Event.objects.create(
            name='Evgeny Grinko',
            category=Category.objects.get(id=1)
        )

        Seat.objects.create(
            seat_no = 1,
            row_no = 1,
            column_no = 1,
            section = Section.objects.get(id=1),
            property = '',
            _isEmpty = True,
            event_no = Event.objects.get(id=1)
        )

    def test_category_serializer_isvalid(self):
        """ Test category isvalid """
        serializer = CategorySerializer(data={"name":"First", "slug":"First"})
        self.assertTrue(serializer.is_valid())

    def test_category_notvalid(self):
        """ Test category notvalid """
        serializer = CategorySerializer(data={"phone":"0902667safs3395"})
        self.assertFalse(serializer.is_valid())

    def test_section_serializer_isvalid(self):
        """ Test section isvalid """
        serializer = SectionSerializer(data={"name":"BALCONY", "rank": "FIRST"})
        self.assertTrue(serializer.is_valid())

    def test_section_notvalid(self):
        """ Test section notvalid """
        serializer = SectionSerializer(data={"name":"BALCONY", "rank": "1st"})
        self.assertFalse(serializer.is_valid())

    def test_event_serializer_isvalid(self):
        """ Test event isvalid """
        category = Category.objects.get(id=1)
        serializer = EventSerializer(data={"name":"Evgeny Grinko","category": category.id})
        self.assertTrue(serializer.is_valid())

    def test_event_notvalid(self):
        """ Test event notvalid """
        serializer = EventSerializer(data={"phone":"0902667safs3395"})
        self.assertFalse(serializer.is_valid())

    def test_seat_serializer_isvalid(self):
        """ Test set isvalid """
        serializer = SeatSerializer(
        data={"seat_no": 1, "row_no": 1, "column_no": 1,
        "section": 1, "booked_by": "neslisahgamze@gmail.com", "property": "BASIC",
        "_isEmpty": True, "event_no": 1 })
        self.assertTrue(serializer.is_valid())

    def test_seat_notvalid(self):
        """ Test set notvalid """
        serializer = SeatSerializer(data={"phone":"0902667safs3395"})
        self.assertFalse(serializer.is_valid())

    # def test_allocate_serializer_isvalid(self):
    #   User.objects.create(email='neslisahgamze@gmail.com')
    #   user = User.objects.get(id=1)
    #   context = {'request': { user }}
    #   serializer = AllocateSerializer(
    #     data={"group_of_users": 1 , "property": "BASIC", "section": 1, "user": 1},
    #     context=context)
    #   print(serializer)
    #   self.assertTrue(serializer.is_valid())

    def test_allocate_notvalid(self):
        """ Test allocate notvalid """
        serializer = AllocateSerializer(data={"phone":"0902667safs3395"})
        self.assertFalse(serializer.is_valid())
