"""
Given an n x n binary matrix, return the length of the shortest clear path from the top-left cell (0,0)
to the bottom-right (n-1, n-1). A clear path moves only through cells containing 0, and here movement is 8-directional
(including diagonals). The length is the number of cells visited. If no path exists, return -1.
Example: [[0,1],[1,0]] → 2. [[0,0,0],[1,1,0],[1,1,0]] → 4. If grid[0][0] or grid[n-1][n-1] is 1 → -1.

Shortest Clear Path in a Binary Matrix — BFS on an implicit grid graph.

WHY BFS AND NOT DFS — the guarantee, not a speedup:
BFS explores in expanding rings: every cell at distance d is fully processed
before any cell at distance d+1. So the FIRST time the target is reached, the
route taken is provably shortest. A single DFS can reach the target by an
arbitrarily long winding path; extracting the shortest from DFS requires
enumerating all paths (exponential). DFS answers reachability; BFS answers
shortest-unweighted.

Design notes:
- visited doubles as the distance array: 0 = unseen, k = reached in k cells
  (start seeded to 1, matching the count-cells-visited spec). Marking AT
  ENQUEUE TIME stamps each cell's distance exactly once and keeps duplicates
  out of the queue.
- Optional early exit when the target is dequeued — sound because of the
  ring guarantee — skips exploring the rest of the reachable region.

Time: O(n^2) (each cell enqueued once)   Space: O(n^2)
"""

from collections import deque


def find_clear_path(grid: list[list[int]]) -> int:
    # here assuming if the grid is empty or none, i’ll return -1
    # denoting no clear path is available.
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
        return -1

    # here visited with non-zero acts as a counter
    visited = [[0 for _ in range(n)] for _ in range(m)]

    q = deque()

    visited[0][0] = 1
    q.append((0, 0))

    def can_enqueue(nd: tuple[int, int]):
        a, b = nd
        if a < 0 or b < 0 or a >= m or b >= n:
            return False

        return visited[a][b] == 0 and grid[a][b] == 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while q:
        x, y = q.popleft()

        # check all 8 directions to find the neighbors
        for dx, dy in directions:
            node = (x + dx, y + dy)
            if can_enqueue(node):
                visited[node[0]][node[1]] = 1 + visited[x][y]
                q.append(node)

    steps = visited[m - 1][n - 1]
    return steps if steps != 0 else -1