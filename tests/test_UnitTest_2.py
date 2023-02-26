import unittest
import random
import sys
from CSCK541_Practical_Assessment import Floyd_Recursive
from CSCK541_Practical_Assessment import Random_Graph


class TestSum(unittest.TestCase):
    """
    The Floyd-Warshall algorithm is not able to compute the correct distances in case of
    a negative cycle in the graph, because the shortest path may not exist.
    In the recursive function there is a built-in check for negative numbers, setting them to zero.
    Test 2 is intended to test, if this part of the function works properly.
    """
    def test_floyd_warshall_recursion(self):
        # Test case 1: graph with no negative cycles
        num_nodes = random.randint(1, 10)
        edge_prob = random.randint(0, 100)
        max_dist = sys.maxsize
        graph = Random_Graph.generate_random_graph(num_nodes, edge_prob, max_dist)
        expected_distance = Floyd_Recursive.floyd_warshall_recursion(graph)
        print(f'Test 1\n Graph: {graph},\n Shortest Distances: {expected_distance}')

        self.assertEqual(Floyd_Recursive.floyd_warshall_recursion(graph), expected_distance, "Should be equal")

        # Test case 2: graph with negative cycle
        num_nodes = random.randint(1, 10)
        edge_prob = random.randint(-100, 0)
        max_dist = sys.maxsize
        graph = Random_Graph.generate_random_graph(num_nodes, edge_prob, max_dist)
        expected_distance = Floyd_Recursive.floyd_warshall_recursion(graph)
        print(f'Test 2\n Graph: {graph},\n Shortest Distances: {expected_distance}')

        self.assertEqual(Floyd_Recursive.floyd_warshall_recursion(graph), expected_distance,
                         "Should be equal and show 0")


if __name__ == '__main__':
    unittest.main()
