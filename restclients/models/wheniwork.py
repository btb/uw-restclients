from django.db import models
from datetime import time


class Account(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    master = models.ForeignKey('self')
    company = models.CharField(max_length=500)

    class Meta:
        db_table = "restclients_wheniwork_account"


class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    employee_code = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "restclients_wheniwork_user"


class Location(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "restclients_wheniwork_location"


class Position(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "restclients_wheniwork_position"


class Site(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    location = models.ForeignKey(Location)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "restclients_wheniwork_site"


class Shift(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account = models.ForeignKey(Account)
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    position = models.ForeignKey(Position)
    site = models.ForeignKey(Site)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.CharField(max_length=350)

    class Meta:
        db_table = "restclients_wheniwork_shifts"


class Request(models.Model):
    STATUS_PENDING = 0
    STATUS_CANCELED = 1
    STATUS_ACCEPTED = 2
    STATUS_EXPIRED = 3

    TYPE_UNPAIDTIMEOFF = 0
    TYPE_PAIDTIMEOFF = 1
    TYPE_SICKLEAVE = 2
    TYPE_HOLIDAY = 3

    id = models.PositiveIntegerField(primary_key=True)
    account = models.ForeignKey(Account)
    user = models.ForeignKey(User)
    creator = models.ForeignKey(User, related_name='+')
    status = models.PositiveSmallIntegerField(choices=(
        (STATUS_PENDING, 'Pending'),
        (STATUS_CANCELED, 'Canceled'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_EXPIRED, 'Expired')))
    type = models.PositiveSmallIntegerField(choices=(
        (TYPE_UNPAIDTIMEOFF, 'Unpaid Time Off'),
        (TYPE_PAIDTIMEOFF, 'Paid Time Off'),
        (TYPE_SICKLEAVE, 'Sick Leave'),
        (TYPE_HOLIDAY, 'Holiday')))
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    canceled_by = models.ForeignKey(User, related_name='+')
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def is_allday(self, tz):
        if self.start_time.astimezone(tz).time() == time(0, 0, 0) \
                and self.end_time.astimezone(tz).time() == time(23, 59, 59):
            return True
        return False

    class Meta:
        db_table = "restclients_wheniwork_request"


class Message(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account = models.ForeignKey(Account)
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)
    swap_id = models.PositiveIntegerField()
    conversation_id = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "restclients_wheniwork_message"
