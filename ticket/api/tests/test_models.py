""" Test """
# pylint: disable=maybe-no-member
from django.test import TestCase

from api.models import Seat
from api.models import Event
from api.models import Category
from api.models import Section

from api.tests.factories import CategoryFactory
from api.tests.factories import EventFactory, SectionFactory
from api.tests.factories import SeatFactory

class ModelsTests(TestCase):
    """ Models test cases """
    def setUp(self):
        """ Set up """

        CategoryFactory(name='First', slug='first')
        SectionFactory(name='High', rank='1st')
        EventFactory(name='Evgeny Grinko', category=Category.objects.get(id=1))
        SeatFactory(event_no = Event.objects.get(id=1))

    def test_category_content(self):
        """ Test category content """
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEqual(expected_object_name, 'First')

    def test_section_content(self):
        """ Test section content """
        section = Section.objects.get(id=1)
        expected_object_name = f'{section.name}'
        self.assertEqual(expected_object_name, 'High')

    def test_event_content(self):
        """ Test event content """
        event = Event.objects.get(id=1)
        expected_object_name= f'{event.name}'
        self.assertEqual(expected_object_name, 'Evgeny Grinko')

    def test_seat_content(self):
        """ Test seat content """
        seat = Seat.objects.get(id=1)
        expected_event_no = f'{seat.event_no.id}'
        self.assertEqual(expected_event_no, '1')
