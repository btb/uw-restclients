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
    location_id = models.IntegerField(max_length=20)
    position_id = models.IntegerField(max_length=20)
    site_id = models.IntegerField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.CharField(max_length=350)

    class Meta:
        db_table = "restclients_wheniwork_shifts"
