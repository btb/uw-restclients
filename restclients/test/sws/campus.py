from django.test import TestCase
from django.conf import settings
from restclients.sws import SWS
from restclients.exceptions import DataFailureException

class SWSTestCampus(TestCase):

    def test_campus(self):
        with self.settings(
                RESTCLIENTS_SWS_DAO_CLASS='restclients.dao_implementation.sws.File'):
            sws = SWS()

            campuses = sws.get_all_campuses()

            self.assertEquals(len(campuses), 3)
