import unittest
from AttendanceChatbotController import *


class AttendanceTest(unittest.TestCase):

    def test_full_attendance(self):
        self.assertEqual(create_attendance(Attendance(displayName='Charline', attendance='ooooo')), {'Charline', '✅|✅|✅|✅|✅'})
        self.assertEqual(create_attendance(Attendance(displayName='Charline', attendance='OOOOO')), {'Charline', '✅|✅|✅|✅|✅'})
        self.assertEqual(create_attendance(Attendance(displayName='Charline', attendance='00000')), {'Charline', '✅|✅|✅|✅|✅'})
        self.assertEqual(create_attendance(Attendance(displayName='Charline', attendance='vvvvv')), {'Charline', '✅|✅|✅|✅|✅'})
        self.assertEqual(create_attendance(Attendance(displayName='Charline', attendance='VVVVV')), {'Charline', '✅|✅|✅|✅|✅'})

    def test_no_attendance(self):
        self.assertEqual(create_attendance(Attendance(displayName='Toto', attendance='xxxxx')), {'Toto', '❌|❌|❌|❌|❌'})
        self.assertEqual(create_attendance(Attendance(displayName='Toto', attendance='XXXXX')), {'Toto', '❌|❌|❌|❌|❌'})
        self.assertEqual(create_attendance(Attendance(displayName='Toto', attendance='nnnnn')), {'Toto', '❌|❌|❌|❌|❌'})
        self.assertEqual(create_attendance(Attendance(displayName='Toto', attendance='NNNNN')), {'Toto', '❌|❌|❌|❌|❌'})

    def test_idk_attendance(self):
        self.assertEqual(create_attendance(Attendance(displayName='Tutu', attendance='?????')), {'Tutu', '❓|❓|❓|❓|❓'})

    def test_some_attendance(self):
        self.assertEqual(create_attendance(Attendance(displayName='Rose', attendance='oooxx')), {'Rose', '✅|✅|✅|❌|❌'})
        self.assertEqual(create_attendance(Attendance(displayName='Rose', attendance='vo0xN')), {'Rose', '✅|✅|✅|❌|❌'})
