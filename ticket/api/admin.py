""" Admin """
from django.contrib import admin

from .models import Ticket, Category, Seat, Section, Event

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Seat)
admin.site.register(Section)
admin.site.register(Event)
