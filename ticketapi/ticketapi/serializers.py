""" Serializers define the API representation. """
from rest_framework import serializers
from django.contrib.auth.models import User
from tickets.models import Ticket, Category, Seat, Section, Event

class UserSerializer(serializers.ModelSerializer):
    """ User serializers """
    class Meta:  # pylint: disable=too-few-public-methods
        """ Class meta docstring """
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
class TicketSerializer(serializers.ModelSerializer): # pylint: disable=too-few-public-methods
    """ Ticket serializers """
    class Meta:  # pylint: disable=too-few-public-methods
        """ Class meta docstring """
        model = Ticket
        fields = (
            'id','title', 'ticket_id','user', 'status', 'content', 'category','created', 'modified')

class CategorySerializer(serializers.ModelSerializer):
    """ Categori serializers """
    class Meta:  # pylint: disable=too-few-public-methods
        """ Class meta docstring """
        model = Category
        fields = ('id', 'name', 'slug')

class SeatSerializer(serializers.ModelSerializer):
    """ Seat serializers """
    class Meta:  # pylint: disable=too-few-public-methods
        """ Class meta docstring """
        model = Seat
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    """ Section serializers """
    class Meta:  # pylint: disable=too-few-public-methods
        """ Class meta docstring """
        model = Section
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    """ Event serializers """
    class Meta:  # pylint: disable=too-few-public-methods
        """ Class meta docstring """
        model = Event
        fields = '__all__'

class AllocateSerializer(serializers.ModelSerializer):
    """ Allocate serializers """
    group_of_users = serializers.IntegerField(min_value=0, max_value=9, default= 1)
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    class Meta:  # pylint: disable=too-few-public-methods
        """ Class meta docstring """
        model = Seat
        fields = ['property', 'group_of_users', 'section', 'user' ]
