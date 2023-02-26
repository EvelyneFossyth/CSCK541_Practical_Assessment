# Define the test case - the sub-function from Floyd_Recursive.py
import sys
import unittest

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]


def shortest_path(i, j, k):
    if k == 0:
        return graph[i][j]
    else:
        return min(shortest_path(i, j, k - 1),
                   shortest_path(i, k - 1, k - 1) + shortest_path(k - 1, j, k - 1))


class TestSubFunction(unittest.TestCase):
    def test_k(self):
        for i in range(len(graph)):
            for j in range(len(graph)):
                self.assertEqual(shortest_path(i, j, 0), graph[i][j], "Should be graph")

    def test_subfunction(self):
        check = 1, 3, 4
        for i in range(len(graph)):
            for j in range(len(graph)):
                self.assertIsNot(shortest_path(i, j, 3), check, "Should not be 1 or 3 or 4")


if __name__ == '__main__':
    unittest.main()
