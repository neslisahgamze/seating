from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test import Client

from api.tests.factories import UserFactory, EventFactory, SeatFactory


class AdminTestCase(TestCase):
    @classmethod
    def setUp(self):
        User.objects.create_superuser(username="username", email="user@example.com", password="password", is_active=True, is_staff=True)

    def test_admin_exists(self):
        test_admin = User.objects.get(username="username")
        self.assertTrue(test_admin.is_superuser)

    def test_admin_login(self):
        user = authenticate(username="username", password="password")
        self.assertEqual(user.email, "user@example.com")

class EventTestCase(TestCase):
    @classmethod
    def setUp(self):
        User.objects.create_superuser(username="username", email="user@example.com", password="password", is_active=True, is_staff=True)
        EventFactory(name="Evgeny Grinko")
        SeatFactory(property="Basic", event_no=EventFactory(name="Evgeny Grinko"))
        self.client = Client()
        self.client_auth = Client()
        self.client_auth.login(username='username', password='password', follow=True)

    def test_event_list(self):
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, 200)

    def test_event_details(self):
        response = self.client_auth.get('/api/events/1/')
        self.assertEqual(response.status_code, 200)

    def test_not_found_event_details(self):
        response = self.client_auth.get('/api/events/3/')
        self.assertEqual(response.status_code, 404)

    def test_find_seats(self):
        response = self.client_auth.post('/api/events/1/find_seats/', { 
            'group_of_users': 1,
            'property': 'Basic',
            'section': 1
        })
        self.assertEqual(response.status_code, 404)

    def test_missing_field_find_seats(self):
        data = { 
            'group_of_users': None,
            'property': 'Basic'
        }
    
        response = self.client_auth.post('/api/events/1/find_seats/', data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
