""" Views """
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import UserSerializer
from api.serializers import TicketSerializer
from api.serializers import CategorySerializer
from api.serializers import SeatSerializer
from api.serializers import SectionSerializer
from api.serializers import EventSerializer
from api.serializers import AllocateSerializer
from api.models import Ticket, Category, Seat, Section, Event

from api.utils import seating_by_size
from api.utils import MinValueError, NotFound

class UserViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """ User view set """
    queryset = User.objects.all()
    serializer_class = UserSerializer
class TicketViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """ Ticket view set """
    queryset = Ticket.objects.all() # pylint: disable=maybe-no-member
    serializer_class = TicketSerializer
class CategoryViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """ Category view set """
    queryset = Category.objects.all() # pylint: disable=maybe-no-member
    serializer_class = CategorySerializer

class SeatViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """ Seat view set """
    queryset = Seat.objects.all() # pylint: disable=maybe-no-member
    serializer_class = SeatSerializer
class SectionViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """ Section view set """
    queryset = Section.objects.all() # pylint: disable=maybe-no-member
    serializer_class = SectionSerializer
class EventViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """ Event view set """
    queryset = Event.objects.all() # pylint: disable=maybe-no-member
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.action == 'find_seats':
            return AllocateSerializer
        return EventSerializer

    @action(methods=["post"], detail=True)
    def find_seats(self, request, **kwargs):
        """ Find seats """
        user_id = self.request.user.id
        user = User.objects.get(pk=user_id).email
        event_no = kwargs['pk']
        _property = request.POST.get('property', None)
        section = request.POST.get('section', None)
        group_of_users = request.POST.get('group_of_users', 0)

        if not group_of_users:
            return Response('Group of user cannot be empty', status=status.HTTP_400_BAD_REQUEST)

        try:
            result = seating_by_size(
                event_no = event_no,
                _property = _property,
                groups_of_users = int(group_of_users),
                section = section,
                user=user)
            return Response(result)
        except MinValueError:
            return Response('User count must be greater than zero',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except NotFound:
            return Response('Not found available seats for the event.',
                            status=status.HTTP_404_NOT_FOUND)