from collections import deque
import time

# Maze Representation
# The maze is a 2D list where:
# 0 = free space (the agent can move here)
# 1 = wall (the agent cannot move here)
maze = [
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # Row 0
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],  # Row 1
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  # Row 2
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],  # Row 3
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],  # Row 4
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],  # Row 5
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],  # Row 6
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],  # Row 7
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],  # Row 8
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # Row 9
]

start = (0, 0)
goal = (9, 9)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def display_maze(maze, path=None):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) == start:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif path and (i, j) in path:
                print(".", end=" ")
            else:
                print("#" if col == 1 else " ", end=" ")
        print()

def bfs(maze, start, goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                queue.append(path + [(new_x, new_y)])
                visited.add((new_x, new_y))
    return None

def dfs(maze, start, goal):
    stack = [[start]]
    visited = set([start])

    while stack:
        path = stack.pop()
        x, y = path[-1]

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                stack.append(path + [(new_x, new_y)])
                visited.add((new_x, new_y))
    return None

start_time = time.time()
bfs_path = bfs(maze, start, goal)
bfs_time = time.time() - start_time

start_time = time.time()
dfs_path = dfs(maze, start, goal)
dfs_time = time.time() - start_time

if bfs_path:
    print("BFS found a path in {:.5f} seconds".format(bfs_time))
    display_maze(maze, bfs_path)
else:
    print("No path found using BFS in {:.5f} seconds".format(bfs_time))

if dfs_path:
    print("DFS found a path in {:.5f} seconds".format(dfs_time))
    display_maze(maze, dfs_path)
else:
    print("No path found using DFS in {:.5f} seconds".format(dfs_time))

if bfs_time < dfs_time:
    print("BFS is faster.")
elif dfs_time < bfs_time:
    print("DFS is faster.")
else:
    print("Both algorithms took the same time.")