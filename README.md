# Maze Solver

This project implements two algorithms to solve a maze. The algorithms used are Breadth-First Search (BFS) and Depth-First Search (DFS). 

## Maze Representation

The maze is represented as a 2D list:

- `0` = free space (the agent can move here)
- `1` = wall (the agent cannot move here)

## Features

- Visual representation of the maze
- Pathfinding using BFS and DFS
- Time comparison between both algorithms

## Usage

1. Clone the repository
2. Run the `maze_solver.py` file
3. Input either `bfs` or `dfs` to choose the algorithm

## Example Maze

BFS found a path in 0.00024 seconds
S #           #     
. #   # # #   #     
. #       #         
.     #     # # #   
. # # #   #     #   
.         #   # #   
. # # #         #   
. . . # # # #   #   
  # . . . . #   #   
      # # . . . . G 
DFS found a path in 0.00013 seconds
S #           #     
. #   # # #   #     
. # . . . #         
. . . # .   # # #   
  # # # . #     #   
. . . . . #   # #   
. # # #         #   
. . . # # # #   #   
  # . . . . #   #   
      # # . . . . G 
DFS is faster.
