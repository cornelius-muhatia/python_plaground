import unittest

def is_palindrome(no):
    """
    Checks if a number is <a href="https://en.wikipedia.org/wiki/Palindrome">Palindrome</a> i.e. 1001 is palindrome.
    Refer to <a href="https://www.programiz.com/c-programming/examples/palindrome-number">Programiz implementation</a>
    :param no: number
    :return: true if number is palindrome otherwise false.
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


class Palindrome(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(is_palindrome(1001))

    def test_case2(self):
        self.assertFalse(is_palindrome(12))

    def test_case3(self):
        self.assertTrue(is_palindrome(110011))

    def test_case4(self):
        self.assertFalse(is_palindrome(1234))


unittest.main()
