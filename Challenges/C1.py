"""
Challenge 1: Spiral Order Traversal of a Matrix Using Recursion

Name: Suppatouch Srinual
ID: 2420210037

Problem: 
Write a recursive Python function to return the elements of a 2D matrix in spiral order. 
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

matrix = [[1, 2, 3, 4]]

def spiral_order(matrix, row):
    if (len(matrix) == 0):
        return []
    else:
        firstIter = [matrix[row][0]] + spiral_order(matrix[row][1:], 0)
        return firstIter

print(spiral_order(matrix, 0))