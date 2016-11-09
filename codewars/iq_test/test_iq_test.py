import unittest

from iq_test.iq_test import iq_test

class IQTestTestCase(unittest.TestCase):

    def test_cases(self):
        self.assertEquals(iq_test("2 4 7 8 10"), 3)
        self.assertEquals(iq_test("1 2 2"), 1)