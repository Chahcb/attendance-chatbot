import unittest
from AttendanceChatbotController import *


class AttendanceTest(unittest.TestCase):

    def test_full_attendance(self):
        self.assertEqual({' ✅ | ✅ | ✅ | ✅ | ✅ '}, create_attendance(Attendance(attendance='ooooo')))
        self.assertEqual({' ✅ | ✅ | ✅ | ✅ | ✅ '}, create_attendance(Attendance(attendance='OOOOO')))
        self.assertEqual({' ✅ | ✅ | ✅ | ✅ | ✅ '}, create_attendance(Attendance(attendance='00000')))
        self.assertEqual({' ✅ | ✅ | ✅ | ✅ | ✅ '}, create_attendance(Attendance(attendance='vvvvv')))
        self.assertEqual({' ✅ | ✅ | ✅ | ✅ | ✅ '}, create_attendance(Attendance(attendance='VVVVV')))
        self.assertEqual({' ✅ | ✅ | ✅ | ✅ | ✅ '}, create_attendance(Attendance(attendance='VvOo0')))

    def test_no_attendance(self):
        self.assertEqual({' ❌ | ❌ | ❌ | ❌ | ❌ '}, create_attendance(Attendance(attendance='xxxxx')))
        self.assertEqual({' ❌ | ❌ | ❌ | ❌ | ❌ '}, create_attendance(Attendance(attendance='XXXXX')))
        self.assertEqual({' ❌ | ❌ | ❌ | ❌ | ❌ '}, create_attendance(Attendance(attendance='nnnnn')))
        self.assertEqual({' ❌ | ❌ | ❌ | ❌ | ❌ '}, create_attendance(Attendance(attendance='NNNNN')))

    def test_idk_attendance(self):
        self.assertEqual({' ❓ | ❓ | ❓ | ❓ | ❓ '}, create_attendance(Attendance(attendance='?????')))

    def test_some_attendance(self):
        self.assertEqual({' ✅ | ✅ | ✅ | ❌ | ❌ '}, create_attendance(Attendance(attendance='oooxx')))
        self.assertEqual({' ✅ | ✅ | ✅ | ❌ | ❌ '}, create_attendance(Attendance(attendance='vo0xN')))

    def test_error_attendance(self):
        self.assertEqual({' ERROR | ERROR | ERROR | ERROR | ERROR '}, create_attendance(Attendance(attendance='dlcsd')))
        self.assertEqual({' ERROR | ERROR | ERROR | ERROR | ERROR '}, create_attendance(Attendance(attendance='DsgQM')))
