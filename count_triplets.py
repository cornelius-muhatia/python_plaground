import unittest


def count_triplets(arr, r):
    """
    Determines number of triplets forming a geometric progression for
    a given r as an integer. Full problem statement can be found at [Hackerrank](http://hr.gs/3cd5m #programming)
    :param arr: an array of integers
    :param r: common ratio
    :return:
    """
    size = len(arr)
    count = 0
    for i in range(0, size):
        sub_count = 1
        j = i + 1
        k = i + 2
        current_val = arr[i]
        first_index = 0
        while j < size:
            if (current_val * r) == arr[j]:
                sub_count = sub_count + 1
                current_val = arr[j]
            if sub_count == 2:
                first_index = j
            if sub_count == 3:
                count = count + 1
                sub_count = 1
                current_val = arr[i]
                if first_index == k:
                    j = k + 1
                    k = k + 2
                else:
                    j = k
                    k = k + 1
            else:
                j = j + 1

    return count


class TestCountTriplets(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(count_triplets([1, 5, 5, 25, 125], 5), 4)

    def test_case2(self):
        self.assertEqual(count_triplets([1, 2, 2, 4], 2), 2)


# unittest.main()
print('Geometry progression', count_triplets([1, 5, 5, 25, 125], 5))
print('Geometry progression', count_triplets([1, 2, 2, 4], 2))
