from django.db import models


class WhenIWorkAccount(models.Model):
    account_id = models.IntegerField(max_length=20)
    company = models.CharField(max_length=500)
    master_id = models.IntegerField(max_length=20)

    class Meta:
        db_table = "restclients_wheniwork_account"


class Shift(models.Model):
    shift_id = models.IntegerField(max_length=20)
    user_id = models.IntegerField(max_length=20)
    account_id = models.IntegerField(max_length=20)
    location_id = models.IntegerField(max_length=20)
    position_id = models.IntegerField(max_length=20)
    site_id = models.IntegerField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.CharField(max_length=350)

    class Meta:
        db_table = "restclients_wheniwork_shifts"


class WhenIWorkUser(models.Model):
    user_id = models.IntegerField(max_length=20)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "restclients_wheniwork_user"


class WhenIWorkLocation(models.Model):
    location_id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "restclients_wheniwork_location"


class WhenIWorkPosition(models.Model):
    position_id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "restclients_wheniwork_position"


class WhenIWorkSite(models.Model):
    site_id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=100, null=True)
    location_id = models.IntegerField(max_length=20)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "restclients_wheniwork_site"
