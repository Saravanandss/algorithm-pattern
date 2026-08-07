"""Universal Sink in a directed graphs (adjacency-matrix form).

A universal sink is a vertex with in-degree n-1 and out-degree 0: every other
vertex points to it, and it points to no one. In the matrix, that means row k
is all zeros and column k is all ones except the diagonal. A graphs has at most
one universal sink.

Key insight — O(n) elimination instead of O(n^2) scanning:
Walk from (0, 0). At (i, j):
  - graphs[i][j] == 1  =>  i is not a sink (a sink's row is all zeros), advance i.
  - graphs[i][j] == 0  =>  j is not a sink (a sink's column is all ones), advance j.
Each step eliminates one candidate in O(1), so one pass leaves a single
survivor. The walk finds the ONLY possible sink but doesn't prove it is one
(the graphs may have none), so a final O(n) verification of that candidate's
row and column is required.

Time: O(n)  Space: O(1)
"""


def find_universal_sink(graph: list[list[int]]):
    """Return the index of the universal sink, or None if there isn't one."""
    if not graph:
        return None
    if len(graph) != len(graph[0]):
        raise ValueError("Adjacency matrix must be square.")

    i, j = 0, 0
    while i < len(graph) and j < len(graph):
        if graph[i][j] == 1:
            i += 1
        else:
            j += 1

    return i if i < len(graph) and is_sink(graph, i) else None


def is_sink(graph: list[list[int]], k: int) -> bool:
    l = len(graph)

    for i in range(l):
        if i != k and graph[i][k] == 0:
            return False
        if graph[k][i] == 1:
            return False

    return True
