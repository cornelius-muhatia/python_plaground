import unittest


def gcd(large, small):
    """
    Get greatest common divisor of 2 integers. For example the gcd of 77 and 22 is 11

    :param large: largest integer
    :param small: smallest integer
    :return: greatest common divisor
    """
    lrg = large
    sml = small
    while True:
        rem = lrg % sml
        if rem == 0:
            return sml
        else:
            lrg = sml
            sml = rem


class GcdTests(unittest.TestCase):

    def gcd_tests(self):
        self.assertEqual(8, gcd(24, 8))
        self.assertEqual(11, gcd(77, 22))
        self.assertEqual(1, gcd(17, 13))


unittest.main()
