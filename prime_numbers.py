import unittest
from math import sqrt


def count_prime_numbers(n):
    """
    Count prime numbers from 1 to the specified number
    :param n: number
    :return: number of prime numbers
    """
    count = 0
    while n > 1:
        is_prime = True
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            count = count + 1
        n = n - 1
    return count


class PrimeNumbers(unittest.TestCase):

    def count_prime_numbers_test(self):
        self.assertEqual(11, count_prime_numbers(31))
        self.assertEqual(6, count_prime_numbers(16))
        self.assertEqual(1229, count_prime_numbers(9999))


unittest.main()

