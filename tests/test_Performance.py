import sys
from timeit import default_timer as timer
from CSCK541_Practical_Assessment import Floyd_Recursive
from CSCK541_Practical_Assessment import Floyd_Iterative

NO_PATH = sys.maxsize

graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

MAX_LENGTH = len(graph[0])


if __name__ == '__main__':
    start = timer()
    Floyd_Iterative.floyd(graph)
    end = timer()

    start2 = timer()
    Floyd_Recursive.floyd_warshall_recursion(graph)
    end2 = timer()

    print(f'Iterative variant: {end - start:.10f}, \n'
          f'Recursive variant: {end2 - start2:.10f}')
