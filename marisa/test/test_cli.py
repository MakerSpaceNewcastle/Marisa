import unittest

from marisa.cli import *


class test_cli(unittest.TestCase):

    def test_time_str_to_seconds_HMS(self):
        self.assertEquals(59, time_str_to_seconds('0:0:59'))
        self.assertEquals(59, time_str_to_seconds('00:00:59'))
        self.assertEquals(60, time_str_to_seconds('0:1:00'))
        self.assertEquals(60, time_str_to_seconds('00:01:00'))
        self.assertEquals(61, time_str_to_seconds('0:1:01'))
        self.assertEquals(61, time_str_to_seconds('00:01:01'))

        self.assertEquals(3599, time_str_to_seconds('0:59:59'))
        self.assertEquals(3599, time_str_to_seconds('00:59:59'))
        self.assertEquals(3600, time_str_to_seconds('1:00:0'))
        self.assertEquals(3600, time_str_to_seconds('01:00:00'))
        self.assertEquals(3601, time_str_to_seconds('1:0:1'))
        self.assertEquals(3601, time_str_to_seconds('01:00:01'))


    def test_time_str_to_seconds_MS(self):
        self.assertEquals(59, time_str_to_seconds('0:59'))
        self.assertEquals(59, time_str_to_seconds('00:59'))
        self.assertEquals(60, time_str_to_seconds('1:00'))
        self.assertEquals(60, time_str_to_seconds('01:00'))
        self.assertEquals(61, time_str_to_seconds('1:01'))
        self.assertEquals(61, time_str_to_seconds('01:01'))


    def test_time_str_to_seconds_S(self):
        self.assertEquals(59, time_str_to_seconds('59'))
        self.assertEquals(60, time_str_to_seconds('60'))
        self.assertEquals(61, time_str_to_seconds('61'))


if __name__ == '__main__':
    unittest.main()
