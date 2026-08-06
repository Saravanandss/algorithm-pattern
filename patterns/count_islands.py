"""
Given an m x n grid of '1's (land) and '0's (water), return the number of islands. An island is a group of 1s
connected horizontally or vertically (not diagonally), surrounded by water. Assume all grid edges are surrounded by water.
Example:
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1   → 3 islands

Number of Islands — connected components, three ways.

The grid is an IMPLICIT GRAPH: each land cell is a node, 4-directional land
adjacency is an edge, and "count islands" = count connected components.

Three implementations, kept deliberately as a learning trail:

v1 — list-of-explicit-sets (first attempt; correct but quadratic).
    Each island is a Python set; merging scans all sets for membership and
    rebuilds. Correct semantics — this IS union-find's meaning — but each
    merge is O(cells), so all-ones grids go O((mn)^2). Measured: 60x60
    all-ones takes ~1.1s vs ~0.007s for v2/v3 (a 160x gap at 3,600 cells).
    Original bug worth remembering: cell keys were f'{i}{j}' strings, so
    (1,12) and (11,2) both hashed as "112" — silent island merges on any
    grid wider than 10. Lesson:  use tuples,
    never separator-less concatenation. Tests under 10 wide never saw it.

v2 — union-find / disjoint-set forest (the efficient encoding of v1's idea).
    Each component is an implicit tree: parent pointers, root = the
    component's representative. find = walk up; union = one pointer write.
    With path compression (write back the root during find) each op is
    approximately ~ constant.

v3 — flood fill (DFS with an explicit stack).
    Scan cells; each unvisited land cell starts a flood that marks its
    whole component; count the floods. O(mn) time and space.
    Lessons: account for all four sides, not just the down and right.
    A deque popped from the right is a stack => this is
    DFS; popleft() would make it BFS. Either traversal counts components —
    BFS only *matters* when shortest path is asked.
"""

from collections import deque


def count_islands(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])
    con: list[set] = []

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                con.append({(i, j)})

    def union_sets(u: set, v: set):
        u_set = [x for x in con if u.issubset(x)]
        v_set = [x for x in con if v.issubset(x)]

        if u_set[0] is not v_set[0]:
            con.append(u_set[0].union(v_set[0]))
            con.remove(u_set[0])
            con.remove(v_set[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and j - 1 >= 0 and grid[i][j - 1]:
                union_sets({(i, j)}, {(i, j - 1)})
            if grid[i][j] == 1 and i - 1 >= 0 and grid[i - 1][j]:
                union_sets({(i, j)}, {(i - 1, j)})

    return len(con)


def count_islands_v2(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    parent: dict[tuple[int, int], tuple[int, int]] = {}

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                parent[(i, j)] = (i, j)

    def find_parent(u: tuple[int, int]) -> tuple[int, int]:
        if parent[u] != u:
            parent[u] = find_parent(parent[u])

        return parent[u]

    def union(u: tuple[int, int], v: tuple[int, int]) -> None:
        parent[find_parent(u)] = find_parent(v)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and j - 1 >= 0 and grid[i][j - 1]:
                union((i, j), (i, j - 1))
            if grid[i][j] == 1 and i - 1 >= 0 and grid[i - 1][j]:
                union((i, j), (i - 1, j))

    return len([item for item in parent if parent[item] == item])


def count_islands_v3(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])

    roots = 0

    visited = [[0 for _ in range(n)] for _ in range(m)]

    def traverse_tree(node: tuple[int, int]):
        x, y = node
        if visited[x][y] == 1:
            return

        nodes = deque()
        nodes.append(node)
        visited[x][y] = 1

        while nodes:
            x, y = nodes.popleft()
            if x + 1 < m and grid[x + 1][y] == 1 and visited[x + 1][y] == 0:
                nodes.append((x + 1, y))
                visited[x + 1][y] = 1
            if y + 1 < n and grid[x][y + 1] == 1 and visited[x][y + 1] == 0:
                nodes.append((x, y + 1))
                visited[x][y + 1] = 1
            if x - 1 >= 0 and grid[x - 1][y] == 1 and visited[x - 1][y] == 0:
                nodes.append((x - 1, y))
                visited[x - 1][y] = 1
            if y - 1 >= 0 and grid[x][y - 1] == 1 and visited[x][y - 1] == 0:
                nodes.append((x, y - 1))
                visited[x][y - 1] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and visited[i][j] != 1:
                traverse_tree((i, j))
                roots += 1

    return roots
