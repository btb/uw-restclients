from django.test import TestCase
from django.conf import settings
from restclients.wheniwork.shifts import Shifts
from restclients.exceptions import DataFailureException

class WhenIWorkTestShifts(TestCase):
    def test_shifts(self):
        with self.settings(
                RESTCLIENTS_WHENIWORK_DAO_CLASS='restclients.dao_implementation.wheniwork.File'):
            wheniwork = Shifts()
            shifts = wheniwork.get_shifts()
            self.assertEquals(len(shifts), 0, "No shifts found")

    def test_due_at_none(self):
        data = {
                "id": "id",
                "user_id": "user_id",
                "location_id": "location_id",
                "position_id": "position_id",
                "site_id": "site_id",
                "start_time": None,
                "end_time": None,
                "notes": "notes"
                }

        shift = Shifts()._shift_from_json(data)
