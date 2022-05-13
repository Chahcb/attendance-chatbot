import unittest
from BOT_controller import *

full_presence = Attendance(displayName='Charline', attendance='ooooo')
dict_full_presence = full_presence.dict()

no_presence = Attendance(displayName='Rose', attendance='xxxxx')
dict_no_presence = no_presence.dict()

empty_presence = Attendance(displayName='Toto', attendance='')
dict_empty_presence = empty_presence.dict()


class testAttendance(unittest.TestCase):

    @staticmethod
    def full_attendance():
        return 'ooooo'

    @staticmethod
    def no_attendance():
        return 'xxxxx'

    @staticmethod
    def empty_attendance():
        return ''

    def test_full_attendance(self):
        self.assertEqual(dict_full_presence['attendance'], self.full_attendance())

    def test_no_attendance(self):
        self.assertEqual(dict_no_presence['attendance'], self.no_attendance())

    def test_empty_attendance(self):
        self.assertEqual(dict_empty_presence['attendance'], self.empty_attendance())
