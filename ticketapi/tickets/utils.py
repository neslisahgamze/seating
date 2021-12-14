""" Utils functions """
from itertools import groupby
from operator import itemgetter

from .models import Seat

def group_seats(seats):
    """ Group seats """
    grouped = []
    seats = sorted(seats, key = itemgetter('row_no'))

    for key, value in groupby(seats, key = itemgetter('row_no')):
        value= list(value)
        new_item = { 'row': key, 'seats': value, 'size': len(value) }
        grouped.append(new_item)

    return grouped

def find_consecutive_number(seats, size):
    """ Find consecutive number """
    num = []
    for i in seats:
        num.append(i['id'])

    if len(num) == 1:
        return num
    grouped = groupby(enumerate(num), key=lambda x: x[0] - x[1])
    all_groups = ([i[1] for i in g] for _, g in grouped)

    for group in all_groups:
        if len(group) == size:
            return group

    return False

def update_seats_unavailable(id_list, user):
    """ Update seat unavailable """
    try:
        Seat.objects.filter(id__in=id_list).update(_isEmpty=False, booked_by=user) # pylint: disable=maybe-no-member
    except Exception:
        pass

def seating_by_size(groups_of_users, user, property = None, event_no = None, section = None):
    """ Seating by size """
    try:
        params = {
            'property' : property,
            'event_no' : event_no,
            '_isEmpty': True,
            'section': section }

        arguments = {}
        for key, value in params.items():
            if value:
                arguments[key] = value

        empty_seats = Seat.objects.filter( # pylint: disable=maybe-no-member
            **arguments).order_by('row_no', 'column_no').values('row_no', 'column_no', 'id')

        if empty_seats is None:
            return

        grouped_seats = group_seats(empty_seats)

        for seat in grouped_seats:
            if groups_of_users <= seat['size']:
                if groups_of_users >= 1:
                    id_list = find_consecutive_number(seat['seats'], groups_of_users)
                    if id_list:
                        update_seats_unavailable(id_list=id_list, user=user)
                        return id_list
    except Exception:
        pass
