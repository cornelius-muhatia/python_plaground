import unittest
from math import sqrt


def sum_divisors(n):
    """
    Sums all divisors of a number. For example given 8; the sum of all divisors is 15 (1, 2, 4, 8)
    :param n: Number
    :return: total divisors
    """
    if n == 1:
        return n
    total = 1 + n
    limit = int(sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            if i * i == n:
                total = total + i
            else:
                total = total + i + (n / i)
    return total


class Divisors(unittest.TestCase):

    def sum_divisors_test(self):
        self.assertEqual(1, sum_divisors(1))
        self.assertEqual(15, sum_divisors(8))
        self.assertEqual(8, sum_divisors(7))
        self.assertEqual(2340, sum_divisors(1000))


unittest.main()
