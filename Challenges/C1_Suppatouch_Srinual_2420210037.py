"""
Challenge 1: Spiral Order Traversal of a Matrix Using Recursion

Name: Suppatouch Srinual
ID: 2420210037

Problem: 
Write a recursive Python function to return the elements of a 2D matrix in spiral order. 
"""
def spiral_traverse(matrix):
    if len(matrix) == 0:
        return []
    
    elif len(matrix[0]) == 1:
        return [row[0] for row in matrix]
    
    top_row = matrix[0]
    right_column = [row[-1] for row in matrix[1:]] if len(matrix[0]) > 1 else []
    bottom_row = matrix[-1][:-1][::-1] if len(matrix) > 1 else []
    left_column = [row[0] for row in matrix[-2:0:-1]] if len(matrix[0]) > 1 else []

    inner_matrix = [row[1:-1] for row in matrix[1:-1]]

    return top_row + right_column + bottom_row + left_column + spiral_traverse(inner_matrix)

# print(spiral_traverse(matrix))

#======================================================================================
# Assertion and Test Cases
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [[1, 2, 3, 4]]

m3 = []

m4 = [
    [1, 2, 3],
    [4, 5, 6]
]

m5 = [[1], [2], [3], [4]]

m6 = [[1]]

m7 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

m8 = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10]
]

m9 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

print(spiral_traverse(m10))

def assert1() -> None:
    assert spiral_traverse(m1) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_traverse(m2) == [1, 2, 3, 4]
    assert spiral_traverse(m3) == []
    assert spiral_traverse(m4) == [1, 2, 3, 6, 5, 4]
    assert spiral_traverse(m5) == [1, 2, 3, 4]
    assert spiral_traverse(m6) == [1]
    assert spiral_traverse(m7) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    assert spiral_traverse(m8) == [1, 2, 3, 7, 10, 9, 8, 4, 5, 6]
    assert spiral_traverse(m9) == [1, 2, 4, 6, 8, 7, 5, 3]
    print("ALL TEST CASES PASSED!")

assert1()

#======================================================================================