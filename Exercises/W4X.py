from array import *

# Exercise 1: Insert and Access Elements.
"""
1. Create an array of integers with values [10, 20, 30, 40, 50].
2. Insert the value 25 at index 2.
3. Print the entire array.
4. Print the element at index 3.
"""
arr1 = array('i', [10, 20, 30, 40, 50])
arr1.insert(2, 25)
print(f'Array after insertion: {list(arr1)}')
print(f'Element at index 3: {arr1[3]}')

# Exercise 2: Update and Delete Elements
"""
1. Create an array of signed integers with values [-10, -20, -30, -40, -50].
2. Update the value at index 1 to -15.
3. Delete the value -40 from the array.
4. Print the final array.
"""
arr2 = array('i', [-10, -20, -30, -40, -50])
arr2[1] = -15
print(f'Array after update: {list(arr2)}')
arr2.remove(-40)
print(f'Array after deletion: {list(arr2)}')

# Exercise 3: Array Manipulation with User Input
"""
1. Ask the user to input n numbers to create an integer array.
2. Insert the number 99 at the second position in the array.
3. Remove all occurrences of the smallest number in the array.
4. Print the final array.
"""
arr3 = array('i', [])
n = int(input("Enter the number of elements: "))

for i in range(n):
    arr3.append(int(input(f"Enter number {i + 1}: ")))

arr3.insert(1, 99)
print(f"Array after insertion: {list(arr3)}")
curr_min: int = min(arr3)
while curr_min in arr3:
    arr3.remove(min(arr3))
print(f'Array after removing smallest element: {list(arr3)}')

# Exercise 4: Create and Access Elements in a 2D Array
"""
1. Create an array of integers with values. [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
2. Print the entire array.
3. Access and print the element at row 2, column 3.
4. Modify the element at row 1, column 2 to 99.
5. Print the modified array.
"""
arr4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"The original Array:\n{arr4}")
print(f"Element at row 2, column 3: {arr4[1][2]}")
arr4[0][1] = 99
print(f"Modified Array:\n{arr4}")

# Exercise 5: Row and Column Operations
"""
1. Create a 2D array [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
2. Print the first row and the last column.
3. Calculate the sum of all elements in each row and print the result as a list.
"""
arr5 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(f'First Row: {arr5[0]}')
lastCol = []
for i in range(len(arr5)):
    lastCol.append(arr5[i][len(arr5[i]) - 1])
print(f'Last Column: {lastCol}')
sumRow = []
for i in range(len(arr5)):
    sum = 0
    for j in range(len(arr5[i])):
        sum += arr5[i][j]
    sumRow.append(sum)
print(f'Sum of Rows: {sumRow}')

# Exercise 3: Dynamic 2D Array with Input
"""
1. Ask the user to input the number of rows and columns for a 2D array.
2. Dynamically create a 2D array filled with 0s.
3. Ask the user to input values for specific position in the array (e.g. row 1, col 1).
4. Print the final array.
"""
x = int(input("Enter the number of rows: "))
y = int(input("Enter the number of columns: "))

arr6 = [[0 for _ in range(y)] for _ in range(x)]
print(arr6)
for i in range(x):
    for j in range(y):
        arr6[i][j] = int(input(f"Enter the value for row {i + 1}, column {j + 1}: "))

# for i in range(x):
#     row = []
#     for j in range(y):
#         row.append(int(input(f"Enter the value for row {i + 1}, column {j + 1}: ")))
#     arr6.append(row)

print(f"Final Array:\n{arr6}")