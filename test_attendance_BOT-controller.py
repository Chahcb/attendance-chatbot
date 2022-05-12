import unittest


class test_attendance(unittest.TestCase):

    def full_attendance(self, attendance):
        return attendance == "ooooo"

    def no_attendance(self, attendance):
        return attendance == "xxxxx"

    def test_full_attendance_should_be_be_true(self):
        self.assertTrue(self.full_attendance("ooooo"))

    def test_no_attendance_should_be_be_true(self):
        self.assertTrue(self.no_attendance("xxxxx"))
