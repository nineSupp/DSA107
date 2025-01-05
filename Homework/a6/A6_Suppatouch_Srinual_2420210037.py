"""
Assignment 6: Tree and Traversal
Name: Suppatouch Srinual
ID: 2420210037


Problem: Maze

Maze Escape
Concept: Create a maze game on an N×N grid with a start position and an exit position. The
 player must write code to move a character from the start to the exit, moving up/down/left/right
 by one cell at a time. Certain cells are walls (impassable) while others are paths (walkable). The
 challenge is to find a way through the maze—preferably the shortest path—to reach the exit.

Challenge Details
    1. Maze Setup
        a. The maze is represented by an NxN grid.
        b. Each cell in the grid can be:
            - 0 (walkable path).
            - 1 (wall/ obstacle).

    2. Movement Rules
        a. From any position, you can move one step at a time in one of four directions: up, down, left, or right.
        b. You must ensure you don't collide with walls (cells marked 1) or move outside the grid boundaries.
    
    3. Goal
        a. Write code to move the character from the start cell to the exit cell sucessfully
"""


from typing import List, Tuple
from collections import deque
import random as rd
import math


class Maze:
    def __init__(self, n: int, start: Tuple[int, int], end: Tuple[int, int], grid: List[List[int]]) -> None:
        if (len(grid) == 0):
            print("No path found, len(grid) = 0")
        else:
            self.n = n
            self.grid = grid
            self.start = start
            self.end = end
            self.w = len(grid)
            self.h = len(grid[0])

            self.path, self.shortest_path = self.find_shortest_path()
            self.display_output()

    def get_allcoordinate(self) -> List[Tuple[int, int]]:
        list_of_coor: List[Tuple[int, int]] = []
        for i in range(self.w):
            for j in range(self.h):
                if self.grid[i][j] == 0:
                    list_of_coor.append((i, j))

        return list_of_coor

    def bfs(self, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[int, List[Tuple[int, int]]]:
        if start == end:
            return 0, [start]

        motions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque([(start, [start])])
        visited = set([start])

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == end:
                return len(path) - 1, path

            for dx, dy in motions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.w and 0 <= ny < self.h and self.grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))

        return math.inf, []

    def find_shortest_path(self) -> Tuple[List[Tuple[int, int]], int]:
        distance, path = self.bfs(self.start, self.end)
        return path, distance

    def display_output(self) -> None:
        to_display_grid: str = ""
        for row in self.grid:
            to_display_grid += str(row) + "\n"

        if self.shortest_path == 0:
            print("No path found")
        else:
            to_display: str = f'Input:\nN={self.w}\nMaze ({self.w}x{self.w})\n{to_display_grid}\nStart: {self.start}\nExit: {self.end}\nPath found:'
            print(to_display)
            print(" -> ".join(map(str, self.path)))
            print(f"Distance = {self.shortest_path} steps")


#==================================================================================================
# Ajarn Test Cases
g: List[List[int]] = [[0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1],
                    [1, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1],
                    [1, 1, 1, 0, 0]]

m = Maze(5, (0, 0), (4, 4), g)

print()

#==================================================================================================
# My Test Cases
g1: List[List[int]] = [[1, 0, 0],
                       [1, 0, 0],
                       [0, 0, 0]]

m1 = Maze(0, (0, 0), (2, 2), g1)

print()

g2: List[List[int]] = []

m2 = Maze(0, (0, 0), (1, 1), g2)

#==================================================================================================