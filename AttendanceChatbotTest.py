import unittest
from AttendanceChatbotController import *


class AttendanceTest(unittest.TestCase):

    def test_full_attendance(self):
        self.assertEqual({"@Jean Michel :  ✅ | ✅ | ✅ | ✅ | ✅ "}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='ooooo', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))
        self.assertEqual({"@Jean Michel :  ✅ | ✅ | ✅ | ✅ | ✅ "}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='OOOOO', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))
        self.assertEqual({"@Jean Michel :  ✅ | ✅ | ✅ | ✅ | ✅ "}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='vvvvv', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))
        self.assertEqual({"@Jean Michel :  ✅ | ✅ | ✅ | ✅ | ✅ "}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='VVVVV', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))
        self.assertEqual({"@Jean Michel :  ✅ | ✅ | ✅ | ✅ | ✅ "}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='00000', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))

    def test_no_attendance(self):
        self.assertEqual({'@Jean Michel :  ❌ | ❌ | ❌ | ❌ | ❌ '}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='xxxxx', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))
        self.assertEqual({'@Jean Michel :  ❌ | ❌ | ❌ | ❌ | ❌ '}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='XXXXX', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))
        self.assertEqual({'@Jean Michel :  ❌ | ❌ | ❌ | ❌ | ❌ '}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='nnnnn', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))
        self.assertEqual({'@Jean Michel :  ❌ | ❌ | ❌ | ❌ | ❌ '}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='NNNNN', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))

    def test_idk_attendance(self):
        self.assertEqual({'@Jean Michel :  ❓ | ❓ | ❓ | ❓ | ❓ '}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='?????', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))

    def test_some_attendance(self):
        self.assertEqual({'@Jean Michel :  ✅ | ✅ | ✅ | ❌ | ❌ '}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='0OvnX', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))
        self.assertEqual({'@Jean Michel :  ✅ | ✅ | ✅ | ❌ | ❌ '}, create_attendance(
            Message(type='MESSAGE', message=Attendance(text='oV0Nx', sender=Name(displayName="Jean Michel")),
                    space=Room(displayName='some room'))))

    def test_error_attendance(self):
        self.assertEqual({'@Jean Michel :  ERROR | ERROR | ERROR | ERROR | ERROR '},
                         create_attendance(Message(type='MESSAGE', message=Attendance(text='ASMQb', sender=Name(
                             displayName="Jean Michel")),
                                                   space=Room(displayName='some room'))))
        self.assertEqual({'@Jean Michel :  ERROR | ERROR | ERROR | ERROR | ERROR '},
                         create_attendance(Message(type='MESSAGE', message=Attendance(text='a8fdh', sender=Name(
                             displayName="Jean Michel")),
                                                   space=Room(displayName='some room'))))
