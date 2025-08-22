import heapq
import math

# 8 possible moves
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def heuristic(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def a_star_search(grid):
    n = len(grid)
    start, goal = (0, 0), (n-1, n-1)

    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = [(heuristic(start, goal), 0, start, [start])]  # (f, g, node, path)
    visited = {start: 0}

    while pq:
        f, g, (x, y), path = heapq.heappop(pq)

        if (x, y) == goal:
            return len(path), path

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                new_g = g + 1
                if (nx, ny) not in visited or new_g < visited[(nx, ny)]:
                    visited[(nx, ny)] = new_g
                    new_f = new_g + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (new_f, new_g, (nx, ny), path+[(nx, ny)]))

    return -1, []

# Example run
if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    length, path = a_star_search(grid)
    print("A* Search → Path length:", length, "Path:", path)

