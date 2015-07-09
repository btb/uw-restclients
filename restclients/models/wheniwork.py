from django.db import models


class WhenIWorkAccount(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    master = models.ForeignKey('self')
    company = models.CharField(max_length=500)

    class Meta:
        db_table = "restclients_wheniwork_account"


class WhenIWorkUser(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    employee_code = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "restclients_wheniwork_user"


class WhenIWorkLocation(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "restclients_wheniwork_location"


class WhenIWorkPosition(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "restclients_wheniwork_position"


class WhenIWorkSite(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    location = models.ForeignKey(WhenIWorkLocation)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "restclients_wheniwork_site"

class WhenIWorkShift(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account = models.ForeignKey(WhenIWorkAccount)
    user = models.ForeignKey(WhenIWorkUser)
    location = models.ForeignKey(WhenIWorkLocation)
    position = models.ForeignKey(WhenIWorkPosition)
    site = models.ForeignKey(WhenIWorkSite)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.CharField(max_length=350)

    class Meta:
        db_table = "restclients_wheniwork_shifts"


class WhenIWorkRequest(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account = models.ForeignKey(WhenIWorkAccount)
    user = models.ForeignKey(WhenIWorkUser)
    creator = models.ForeignKey(WhenIWorkUser, related_name='+')
    status = models.PositiveSmallIntegerField()
    type = models.PositiveSmallIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    canceled_by = models.ForeignKey(WhenIWorkUser, related_name='+')
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "restclients_wheniwork_request"
