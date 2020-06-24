import unittest


def rotate90_clockwise(matrix):
    """
    Rotate array 90 degrees clockwise. Modified from:<br/>
    <a href="https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/">GeeksForGeeks</a>
    :param matrix: array representing a squared matrix
    """
    size = len(matrix)
    for i in range(0, int(size/2)):
        last_idx = size - 1 - i
        for j in range(i, last_idx):
            temp = matrix[i][j]
            # move elements to the right
            matrix[i][j] = matrix[size - 1 - j][i]
            # move elements vertically up from the left
            matrix[size - 1 - j][i] = matrix[last_idx][size - 1 - j]
            # move elements to the left from the bottom
            matrix[last_idx][size - 1 - j] = matrix[j][last_idx]
            matrix[j][last_idx] = temp


# class MatrixTest(unittest.TestCase):
#
#     def __init__(self):
#         super().__init__()
#         self.rotate90_clockwise_test()
#
#     def rotate90_clockwise_test(self):
#         matrix = [
#             [1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]
#         ]
#         self.assert_array([], matrix)
#
#     def assert_array(self, array1, array2):
#         arr1_size = len(array1)
#         arr2_size = len(array2)
#         self.assertEqual(arr1_size, arr2_size, "Different array sizes "
#                          + str(arr1_size) + " != " + str(arr2_size))
#         for i in range(0, arr1_size):
#             for j in range(0, arr1_size):
#                 self.assertEqual(array1[i][j], array2[i][j], "Elements at index (" + str(i) + "," + str(j) + ") don't match")
#
#
# unittest.main()
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
rotate90_clockwise(matrix)
print(matrix)
