import unittest


def repeated_string(s, n):
    """
    Returns and integer representing the number of occurrences of a
    in the prefix of length n in the infinitely repeating string

    :param s: target string
    :param n: repeated string final length
    :return: number of occurrence of "a" character
    """
    str_len = len(s)
    count = repeated_len(s, n)
    if n > str_len:
        count = count * int(n/str_len)
        count = count + repeated_len(s, n%str_len)
    return count


def repeated_len(s, n):
    """
    Counts occurrence of a in a string for only n characters. In cases where n is greater than the string length,
    n is ignored

    :param s: target string
    :param n: target length
    :return: "a" occurrence count
    """
    count = 0
    i = 1
    for c in s:
        if i > n:
            break
        if c == "a":
            count += 1
        i += 1
    return count


class TestRepeatedStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(2, repeated_string("abcac", 5), "Test 1")

    def test2(self):
        self.assertEqual(4, repeated_string("abcac", 10), "Test 2")

    def test3(self):
        self.assertEqual(3, repeated_string("abcac", 6), "Test 3")

    def test4(self):
        self.assertEqual(1, repeated_string("abcac", 1), "Test 4")


unittest.main()
