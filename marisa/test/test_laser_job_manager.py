import unittest

from marisa.laser_jab_manager import *


class test_laser_job_manager(unittest.TestCase):

    def test_seconds_to_hms(self):
        self.assertEqual((0, 0, 59), seconds_to_hms(59))
        self.assertEqual((0, 1, 0), seconds_to_hms(60))
        self.assertEqual((0, 1, 1), seconds_to_hms(61))

        self.assertEqual((0, 59, 59), seconds_to_hms(3599))
        self.assertEqual((1, 0, 0), seconds_to_hms(3600))
        self.assertEqual((1, 0, 1), seconds_to_hms(3601))

        self.assertEqual((0, 0, 50), seconds_to_hms(50))
        self.assertEqual((0, 5, 0), seconds_to_hms(300))


if __name__ == '__main__':
    unittest.main()
