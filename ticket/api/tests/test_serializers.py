""" Test """
# pylint: disable=maybe-no-member
from django.test import TestCase

from api.tests.factories import SeatFactory
from api.tests.factories import EventFactory
from api.tests.factories import CategoryFactory
from api.tests.factories import SectionFactory

from api.serializers import SeatSerializer
from api.serializers import EventSerializer
from api.serializers import CategorySerializer
from api.serializers import SectionSerializer
from api.serializers import AllocateSerializer

class SerializersTests(TestCase):
    """ Serializers tests """
    def setUp(self):
        """ Set up """
        CategoryFactory(
            name='First',
            slug='first'
        )

        SectionFactory(
            name='High',
            rank='1st'
        )

        EventFactory(
            name='Evgeny Grinko',
            category=CategoryFactory(name='First')
        )

        SeatFactory(
            seat_no = 1,
            row_no = 1,
            column_no = 1,
            section = SectionFactory(),
            property = '',
            _isEmpty = True,
            event_no = EventFactory(name='Evgeny Grinko')
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
        category = CategoryFactory()
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

    def test_allocate_notvalid(self):
        """ Test allocate notvalid """
        serializer = AllocateSerializer(data={"phone":"0902667safs3395"})
        self.assertFalse(serializer.is_valid())
