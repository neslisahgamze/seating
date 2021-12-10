""" Models """
import uuid
from enum import Enum
from django.db import models
from django.contrib.auth.models import User

def generate_ticket_id():
    """ Function generates ticket id"""
    return str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1] #generate unique ticket id

class PropertiesType(Enum):
    """ PropertiesType """
    BASIC = "Basic"
    AISLE = "Aisle"
    FRONT = "Front"
    HIGH = "High"

    @classmethod
    def choices(cls):
        """ Return choices"""
        return tuple((i.name, i.value) for i in cls)

class RanksType(Enum):
    """ RanksType """
    FIRST = "1st"
    SECOND = "2nd"
    THIRD = "3rd"

    @classmethod
    def choices(cls):
        """ Return choices"""
        return tuple((i.name, i.value) for i in cls)

class SectionType(Enum):
    """ SectionType """
    BALCONY = "balcony"
    MAIN_HALL = "main hall"

    @classmethod
    def choices(cls):
        """ Return choices"""
        return tuple((i.name, i.value) for i in cls)

class Status(Enum):
    """ Status """
    PENDING = "pending"
    COMPLETED = "completed"

    @classmethod
    def choices(cls):
        """ Return choices"""
        return tuple((i.name, i.value) for i in cls)

class Ticket(models.Model):
    """ Ticket model"""
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    status = models.CharField(choices=Status.choices(), max_length=155, default="pending")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.ticket_id}'

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = generate_ticket_id()

        super().save(*args, **kwargs) # Call the real   save() method

    class Meta: # pylint: disable=too-few-public-methods
        """ class """
        ordering = ["-created"]

class Category(models.Model):
    """ Category model"""
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self): # pylint: disable=too-few-public-methods
        return str(self.name)

class Section(models.Model):
    """ Section model"""
    name = models.CharField(choices=SectionType.choices(), max_length=200, blank=True, )
    rank = models.CharField(choices=RanksType.choices(), max_length=155, null=True, blank=True)

    def __str__(self):
        if self.rank:
            return f'{self.rank} - {self.name}'
        return f'{self.name}'

class Event(models.Model):
    """ Event model"""
    name = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Seat(models.Model):
    """ Seat model"""
    seat_no = models.PositiveSmallIntegerField(blank=False, null=False)
    row_no = models.PositiveSmallIntegerField(blank=False, null=False)
    column_no = models.PositiveSmallIntegerField(blank=False, null=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    booked_by = models.EmailField(max_length = 254, blank=True, null=True)
    property = models.CharField(choices=PropertiesType.choices(), max_length= 120)
    isEmpty = models.BooleanField(null=True, blank=True, default=True)
    event_no = models.ForeignKey(Event, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return f'{self.seat_no} - {self.section}'

    def pre_save(self, *args, **kwargs):
        """ pre_save """
        if self.property is not PropertiesType.HIGH.name:
            self.section = Section(name= SectionType.BALCONY)
        super().save(*args, **kwargs)

    class Meta: # pylint: disable=too-few-public-methods
        """ class """
        ordering = ["row_no", "column_no"]
