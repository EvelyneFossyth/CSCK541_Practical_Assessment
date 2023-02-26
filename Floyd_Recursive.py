# A possible implementation of the Floyd-Warshall algorithm using recursion

# Import the module needed
import sys
# Define a constant representing the maximum distance between nodes in the graph
NO_PATH = sys.maxsize
# Define the given graph as a 2-dimensional list
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
# Define a variable representing the number of nodes in the graph
MAX_LENGTH = len(graph[0])


# Define a recursive function that applies the Floyd Warshall algorithm to a graph
def floyd_warshall_recursion(graph):
    """
    Compute the shortest path between all pairs of nodes in a graph using the
    Floyd-Warshall algorithm, implemented recursively.

    Args:
        graph: A square matrix representing a weighted directed graph. In this case the graph is given
        as a 2-dimensional list.

    Returns:
        A matrix, where the element at index (i, j) is the shortest distance between nodes i and j.
    """
    # Define a sub-function that calculates the shortest path between all nodes
    def shortest_path(i, j, k):
        """
        The sub-function uses recursion to compute the shortest path between the i-th and j-th nodes,
        considering all possible intermediate nodes up to k-1. The value of k is decreased with each
        recursive call until it reaches 0, at which point the function returns the distance between
        the i-th and j-th nodes from the original graph.

        Parameter:
        i - start node as integer
        j - end node as integer
        k - intermediate node as integer
        return - an integer, as long as the elements of the graph parameter are integers; otherwise can be a float
        """
        # Base case
        if k == 0:
            return graph[i][j]
        # Recursive case
        else:
            return min(shortest_path(i, j, k - 1),
                       shortest_path(i, k - 1, k - 1) + shortest_path(k - 1, j, k - 1))
    # Call the function recursively with the sub-function as input
    distance = [[shortest_path(i, j, MAX_LENGTH) for j in range(MAX_LENGTH)] for i in range(MAX_LENGTH)]
    # Return the list of the shortest paths
    return distance


if __name__ == '__main__':
    distance = floyd_warshall_recursion(graph)
    print(distance)
