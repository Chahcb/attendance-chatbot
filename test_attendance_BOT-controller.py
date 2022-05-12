import unittest
from BOT_controller import *

class test_attendance(unittest.TestCase):

    def full_attendance(self):
        return "ooooo"

    def no_attendance(self):
        return "xxxxx"

    def test_attendance(self):
        if self.assertEqual("ooooo", self.full_attendance()):
            return "full présence"

        elif self.assertEqual("xxxxx", self.no_attendance()):
            return "No présence"