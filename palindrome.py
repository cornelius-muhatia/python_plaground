import unittest

def is_palindrome(no):
    """
    Checks if a number is <a href="https://en.wikipedia.org/wiki/Palindrome">Palindrome</a> i.e. 1001 is palindrome.
    Refer to <a href="https://www.programiz.com/c-programming/examples/palindrome-number">Programiz implementation</a>
    :param no: number
    :return: True if number is palindrome otherwise False.
    """
    head = no
    tail = 0
    while head > 0:
        rem = head % 10
        tail = (tail * 10) + rem
        head = int(head / 10)
        if tail == head:
            return True
    return False


def get_longest_palindrome(str):
    n = len(str)
    start_idx = 0
    end_idx = 0
    for i in range(0, n):
        odd_start_idx = 0
        odd_end_idx = 2
        even_start_idx = 0
        even_end_idx = 1

        for j in range(i, n):
            while odd_start_idx >= 0 and odd_end_idx < n:
                if str[odd_start_idx] == str[odd_end_idx]:
                    if (end_idx - start_idx) < (odd_end_idx - odd_start_idx):
                        end_idx = odd_end_idx
                        start_idx = odd_start_idx
                    odd_start_idx = odd_start_idx - 1
                    odd_end_idx = odd_end_idx + 1
                else:
                    odd_start_idx = (j+1) - 1
                    odd_end_idx = (j+1) + 1
                    break

            while even_start_idx >= 0 and even_end_idx < n:
                if str[even_start_idx] == str[even_end_idx]:
                    if (end_idx - start_idx) < (even_end_idx - even_start_idx):
                        end_idx = even_end_idx
                        start_idx = even_start_idx
                    even_start_idx = even_start_idx - 1
                    even_end_idx = even_end_idx + 1
                else:
                    even_start_idx = (j+1)
                    even_end_idx = (j+1) + 1
                    break

    return str[start_idx: end_idx + 1]


class Palindrome(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(is_palindrome(1001))

    def test_case2(self):
        self.assertFalse(is_palindrome(12))

    def test_case3(self):
        self.assertTrue(is_palindrome(110011))

    def test_case4(self):
        self.assertFalse(is_palindrome(1234))

    def test_longest_palindrome1(self):
        self.assertEqual("nolon", get_longest_palindrome("nolon"))

    def test_longest_palindrome2(self):
        self.assertEqual("noon", get_longest_palindrome("noonn"))


unittest.main()
