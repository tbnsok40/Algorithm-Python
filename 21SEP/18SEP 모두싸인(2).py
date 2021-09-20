from itertools import combinations
import heapq
from collections import deque


def solution(grid):
    R = len(grid)
    C = len(grid[0])
    queue = deque()
    for r in range(R):
        for c in range(C):
            if (r == 0 and c == 0) or (r == (R - 1) and c == (C - 1) ):
                continue
            else:
                while queue:
                    if r + 1 < R:
                        queue.append(grid[r + 1][c])
                    if c + 1 < C:
                        queue.append(grid[r][c + 1])


                print(r, c)



    return

grid = [[1, 8, 3, 2], [7, 4, 6, 5]]

print(solution(grid))
