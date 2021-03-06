""" Api urls """
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api.views import UserViewSet
from api.views import TicketViewSet
from api.views import CategoryViewSet
from api.views import SeatViewSet
from api.views import SectionViewSet
from api.views import EventViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api/events/<int:pk>/seats', EventViewSet.as_view({"post": "find_seats"})),
    path('openapi/', get_schema_view(
        title="Ticket Service",
        description="API for seating algorithm"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
