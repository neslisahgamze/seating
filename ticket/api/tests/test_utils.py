""" Test utils """
from django.test import TestCase

from api.utils import group_seats
from api.utils import find_consecutive_number

class SimpleTest(TestCase):
    """ Simple test class """
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_group_seats(self):
        """ Test group seats func """
        seats = [{'row_no': 1, 'column_no': 1, 'id': 1}]
        expected_result = [{'row': 1, 'seats': [{'row_no': 1, 'column_no': 1, 'id': 1}], 'size': 1}]
        grouped_seats = group_seats(seats)
        self.assertEqual(grouped_seats, expected_result)

    def test_find_consecutive_number(self):
        """ Test find consecutive number func """
        seats = [{'row_no': 1, 'column_no': 1, 'id': 1}]
        size = 2
        consecutive_number = find_consecutive_number(seats, size)
        expected_result = False
        self.assertEqual(consecutive_number, expected_result)

    def test_success_find_consecutive_number(self):
        """ Test find consecutive number func """
        seats = [{'row_no': 1, 'column_no': 1, 'id': 1}]
        size = 1
        consecutive_number = find_consecutive_number(seats, size)
        expected_result = [1]
        self.assertEqual(consecutive_number, expected_result)
