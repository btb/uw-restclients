from django.test import TestCase
from django.conf import settings
from restclients.wheniwork.account import Accounts as WhenIWork
from restclients.exceptions import DataFailureException

class WhenIWorkTestAccounts(TestCase):

    def test_account(self):
        with self.settings(
                RESTCLIENTS_WHENIWORK_DAO_CLASS='restclients.dao_implementation.wheniwork.File'):
            wheniwork = WhenIWork()

            account = wheniwork.get_account(341132)
            self.assertEquals(account.id, 341132)
            self.assertEquals(account.company, "UW-IT CTE", "Has proper name")
            self.assertEquals(account.master_id, 0)
