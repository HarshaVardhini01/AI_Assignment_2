import heapq
import math

# 8 possible moves
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def heuristic(a, b):
    # Euclidean distance
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def best_first_search(grid):
    n = len(grid)
    start, goal = (0, 0), (n-1, n-1)

    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = [(heuristic(start, goal), start, [start])]  # (h, node, path)
    visited = set([start])

    while pq:
        h, (x, y), path = heapq.heappop(pq)

        if (x, y) == goal:
            return len(path), path

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(pq, (heuristic((nx, ny), goal), (nx, ny), path+[(nx, ny)]))

    return -1, []

# Example run
if __name__ == "__main__":
    grid = [[0,1],[1,0]]
    length, path = best_first_search(grid)
    print("Best First Search → Path length:", length, "Path:", path)

