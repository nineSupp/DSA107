"""
Assignment 5

Name: Suppatouch Srinual
ID: 2420210037
"""
#==============================================================================================
"""
Problem 1: Valid Parentheses Checker (Using Stack!)

Description:
Given a string s consisting only of the characters '(', ')', '}', '{', '[', and ']'. Write a
python function is_balanced(s) that uses a stack to determine wheter the parentheses/ brackets
in the string are balanced. The rules for a balanced string are:
    1. Every opening bracket has a corresponding closing bracket of the same type.
    2. Brackets must close in the correct order (e.g. "(] is invalid even though each charac
       -ter has a match of some type).

Input: s
Output: Return true if s is balanced, otherwise false.

Examples:
    1. s = "()" -> True
    2. s = "()[]{}" -> True
    3. s = "(]" -> False
    4. s = "([)]" -> False
    5. s = "{[]}" -> True

Constraints:
    1. The length of s can be up to 10^5 characters.
    2. s may contain only the characters () {} [].
"""

class FixedStack:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.stack = []
        self.top = -1

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top == self.capacity -1

    def size(self) -> int:
        return len(self.stack)

    def push(self, value: str) -> None:
        if self.is_full():
            # print(f"Stack is full, Cannot push {value}")
            return None
        self.top += 1
        if self.top < len(self.stack):
            self.stack[self.top] = value
        else:
            self.stack.append(value)

    def peak(self) -> int:
        if self.is_empty():
            # print("stack is empty. No top element.")
            return None
        else:
            return self.stack[self.top]
        
    def pop(self) -> None:
        if self.is_empty():
            # print("Stack is emmpty. Cannot pop")
            return None
        else:
            self.stack.pop(self.top)
            self.top -= 1


def is_balanced(s: str) -> bool:
    tempStack: FixedStack = FixedStack(len(s))
    expectableChar = ["(", ")", "[", "]", "{", "}"]
    mapping: dict[str, str] = {"(" : ")", "[" : "]", "{" : "}"}

    for char in s:
        if char in mapping:
            tempStack.push(char)
        else:
            top: str = tempStack.peak()
            if char in expectableChar:
                if (char == ")" and top != "(") or (char == "]" and top != "[") or (char == "}" and top != "{"):
                    return False
                else:
                    tempStack.pop()
            else:
                continue

    return tempStack.size() == 0

"""
Ajarn Test Cases:
"""
print(is_balanced("()"))            # True
print(is_balanced("()[]{}"))        # True
print(is_balanced("(]"))            # False
print(is_balanced("([}]"))          # False
print(is_balanced("{(a+b)*[c-d]}"))          # True

"""
My Test Cases:
"""
# All Valid Parentheses
def tc1() -> None:
    assert is_balanced("()") == True
    assert is_balanced("()[]{}") == True
    assert is_balanced("{[()]}") == True
    assert is_balanced("{[]}") == True
    assert is_balanced("((()))") == True
    assert is_balanced("[()]{}") == True
    assert is_balanced("{{{{}}}}") == True
    assert is_balanced("([]{})") == True
    assert is_balanced("{([])}") == True
    assert is_balanced("{[({})]}") == True
    print("ALL TEST CASES 1 PASSED!")

# All Invalid Parentheses
def tc2() -> None:
    assert is_balanced("(") == False
    assert is_balanced(")") == False                   # Stack empty, No top.
    assert is_balanced("([)]") == False
    assert is_balanced("{[}") == False
    assert is_balanced("{(])}") == False
    assert is_balanced("({)}") == False
    assert is_balanced("(((()") == False
    assert is_balanced(")))") == False                # Stack empty, No top.
    assert is_balanced("({}})") == False
    assert is_balanced("[]}{") == False               # Stack empty, No top.
    print("ALL TEST CASES 2 PASSED!")

# # Edge Cases``
def tc3() -> None:
    assert is_balanced("") == True                  # Empty string
    assert is_balanced(" ") == True                 # Only spaces
    assert is_balanced("a+b") == True               # No parentheses
    assert is_balanced("([])a+b") == True           # Parentheses with letters
    assert is_balanced("{(a+b)*[c-d]}") == True     # Complex expressions
    assert is_balanced("((a)") == False             # Unbalanced with text
    assert is_balanced("(((b+c)]") == False         # Mismatched parentheses
    assert is_balanced("(()") == False              # Missing closing
    assert is_balanced("())") == False              # Missing opening
    assert is_balanced("[[") == False               # Multiple missing closings
    print("ALL TEST CASES 3 PASSED!")

tc1()
tc2()
tc3()
#==============================================================================================

#==============================================================================================
"""
Problem 2: Treasure Hunt Game (Using Queues!)

Description:
You are leading a team of adventurers to find treasure on an island represented as a grid. The
treasure is hidden at specific locations, and you must direct your team to collect the in the
shortest time possible.

Game Rules:
    1. The island is represented as a 2D grid of size (n x nn) X (nn xn).
        a. 0 - represents an empty cell.
        b. 1 - represents the adventurer's starting point.
        c. T - represents treasure locations.
        d. x - represents obstacles.
    2. Adventurers can move up, down, left, or right. But they cannot move into obstacles.
    3. Your task is to find the shortest path to collect all treasures.

Examples:
    Grid: m = [
            [1, 0, 0, T],
            [X, X, 0, T],
            [0, 0, 0, 0],
            [T, 0, X, T]
        ]

Output:
    # Starts at (0, 0) collect all treasures.
    game = TreasureHunt(grid)
    print(game.find_treasures())    # Output: 11
"""

from collections import deque
from typing import List
from typing import Tuple
import math

class QueueUsingList:
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self, item) -> None:
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Dequeue unable to perform from empty list.")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class TreasureHunt:
    def __init__(self, grid: List[List[str]]) -> None:
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        self.coor_treasure = []
        self.q = QueueUsingList()
        self.startingPo = None
        self.getStart()

    def getStart(self) -> None:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == "1":
                    self.startingPo = (i, j)
                elif self.grid[i][j] == "T":
                    self.coor_treasure.append((i, j))
                else:
                    continue

    def all_possible_paths(self, coor: Tuple[int, int], to_reach: Tuple[int, int]) -> int:
        queue = deque([coor])
        distance: int = 0
        visited_cell = set()
        visited_cell.add(self.startingPo)
        motion: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            for i in range(len(queue)):
                q, p = queue.popleft()

                if (q, p) == to_reach:
                    return distance
                
                else:
                    for x, y in motion:
                        xx, yy = q + x, p + y
                        
                        if (0 <= xx < self.n) and (0 <= yy < self.m) and ((xx, yy) not in visited_cell) and self.grid[xx][yy] != "X":
                            visited_cell.add((xx, yy))
                            queue.append((xx, yy))

            distance += 1

        return 0

    def find_treasures(self) -> int:
        if len(self.grid) == 0:
            return 0
        else:
            distance_travel: int = 0
            current_position: Tuple[int, int] = self.startingPo

            while self.coor_treasure:
                expected_dist = math.inf
                next_position = None

                for treasure in self.coor_treasure:
                    dist_to_treasure = self.all_possible_paths(current_position, treasure)
                    if dist_to_treasure != 0 and dist_to_treasure < expected_dist:
                        expected_dist = dist_to_treasure
                        next_position = treasure

                if next_position is None:
                    return 0

                distance_travel += expected_dist
                current_position = next_position
                self.coor_treasure.remove(next_position)

            return distance_travel

grid: List[List[str]] = [["1", "0", "0", "T"], 
                        ["X", "X", "0", "T"],
                        ["0", "0", "0", "0"],
                        ["T", "0", "X", "T"]]

grid2: List[List[str]] = [["X", "X", "X", "T"], 
                        ["X", "T", "0", "T"],
                        ["X", "X", "X", "0"],
                        ["1", "0", "0", "T"]]

grid3: List[List[str]] = [[]]

grid4: List[List[str]] = [["0", "T", "0"],
                          ["X", "1", "0"],
                          ["X", "T", "0"]]

"""
Ajarn Test Cases:
"""
game = TreasureHunt(grid)
print(game.find_treasures())
"""
My Test Cases:
"""
game2 = TreasureHunt(grid2)
print(game2.find_treasures())
game3 = TreasureHunt(grid3)
print(game3.find_treasures())
game4 = TreasureHunt(grid4)
print(game4.find_treasures())

#==============================================================================================
