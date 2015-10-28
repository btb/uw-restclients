from django.test import TestCase
from restclients.util.summer_term import is_a_term, is_b_term,\
    is_full_summer_term

class SummerTermTest(TestCase):

    def test_summer_terms(self):
        self.assertTrue(is_a_term("A-term"))
        self.assertTrue(is_b_term("B-term"))
        self.assertTrue(is_full_summer_term("Full-term"))
        self.assertFalse(is_full_summer_term("A-term"))
        self.assertFalse(is_full_summer_term("B-term"))
