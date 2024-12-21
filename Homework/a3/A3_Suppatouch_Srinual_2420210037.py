"""
Assignment 2

Name: Suppatouch Srinual
ID: 2420210037
"""
#==============================================================================================
"""
Problem 1: Valid Parentheses Checker

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

from typing import List

class fixedStack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1


def is_balanced(s: str) -> bool:
    stack: List[str] = []
    dex: int = 0
    while dex < len(s):
        if s[dex] == "(":
            stack.append("(")
        elif s[dex] == "{":
            stack.append("{")
        elif s[dex] == "[":
            stack.append("[")
        else:
            if s[dex] == ")" and stack[len(stack) - 1] == "(":
                stack.pop(len(stack) - 1)
            elif s[dex] == "}" and stack[len(stack) - 1] == "{":
                stack.pop(len(stack) - 1)
            elif s[dex] == "]" and stack[len(stack) - 1] == "[" :
                stack.pop(len(stack) - 1)
            else:
                return False
        dex += 1

    return stack == []

print(is_balanced("()"))
print(is_balanced("()[]{}"))
print(is_balanced("(]"))
print(is_balanced("([)]"))
print(is_balanced("{[]}"))
is_balanced("([])]")

# print(is_balanced("([])]"))
#==============================================================================================

#==============================================================================================
"""
Problem 2: Treasure Hunt Gamme Using Queues

You are leading a team of adventurers to find treasure on an island represented as a grid. The
teasure is hidden at specific locations, and you must direct your team to collect them in the
shortest time possible

Game Rules:
    1. The island is represented as a 2D grid of size n x m X m x n.
        a. 0 represent an emmpty cell.
        b. 1 represent the adventurers starting point.
        c. T represent treasure locations.
        d. X represent obstacles.
    2. Adventurers can move up, down, left, or right. But they cannot move into obstacles.
    3. Your task is to find the shortest path to collect all treasures.
"""
# class queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, item):
#         self.queue.append(item)

    

# class TreasureHunt:
#     def __init__(self, grid: List[List[str]]):
#         if grid == []:
#             self.grid = self.generate_grid()
#         else:
#             self.grid = grid

#     def generate_grid() -> List[List[str]]:


#     def find_treasures() -> int:


#==============================================================================================
