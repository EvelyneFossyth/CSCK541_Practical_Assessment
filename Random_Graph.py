import random
import sys
# Represent a maximum value that can be stored in a variable of type int in Python
MAX_LENGTH = sys.maxsize


def generate_random_graph(num_nodes, edge_prob, MAX_LENGTH):
    """
    Produce a random directed graph with the given number of nodes and edge probability.
    For each pair of nodes (i, j) where i < j, an edge is created with probability edge_prob.
    To each edge a random distance between 1 and infinity (represented as MAX_LENGTH) is assigned.
    Since the graph is directed, the distance is assigned to the (i, j) edges only.

    Args:
        num_nodes - number of nodes in the graph
        edge_prob - the number of possible edges in the graph
        MAX_LENGTH - maximal possible distance between the nodes

    Returns:
        A random matrix with the given number of lists and elements' probability
    """
    # Initialize an empty directed graph
    graph = [[0] * num_nodes for i in range(num_nodes)]

    # Add edges to the graph with the given probability
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_prob:
                weight = random.randint(1, MAX_LENGTH)
                graph[i][j] = weight

    # Assume that, if start_node and end_node are the same, then the distance would be zero
    for i in range(num_nodes):
        graph[i][i] = 0
    return graph


# Example 1:
# Call the function with 4 nodes and edge probability of my birthday and
# the distance equal to the distance from Earth to Sun
if __name__ == '__main__':
    print(generate_random_graph(4, 421981, 150*1000*1000))


# Example 2:
# Make the function more independent of the user input changing all numbers to randomly generated numbers
if __name__ == '__main__':
    num_nodes = random.randint(1, 52)
    edge_prob = random.randint(0, 421981)
    print(generate_random_graph(num_nodes, edge_prob, MAX_LENGTH))
