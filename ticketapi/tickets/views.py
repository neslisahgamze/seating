""" Views """
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ticketapi.serializers import UserSerializer
from ticketapi.serializers import TicketSerializer
from ticketapi.serializers import CategorySerializer
from ticketapi.serializers import SeatSerializer
from ticketapi.serializers import SectionSerializer
from ticketapi.serializers import EventSerializer
from ticketapi.serializers import AllocateSerializer
from tickets.models import Ticket, Category, Seat, Section, Event

from tickets.utils import seating_by_size

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
        event_no = kwargs['pk']
        property = request.POST.get('property', None)
        section = request.POST.get('section', None)
        group_of_users = request.POST.get('group_of_users', None)
        user = User.objects.filter(id=user_id).values_list('email', flat=True)[0]
        result = seating_by_size(
            event_no = event_no,
            property = property,
            groups_of_users = int(group_of_users),
            section = section,
            user=user)
        if result:
            return Response(result)
        return Response('Error occured',
                        status=status.HTTP_400_BAD_REQUEST)
