"""
Assignment 2

Name: Suppatouch Srinual
ID: 2420210037

# Instructions:
Implement the following problems
    P1) Combine Two List (Intermediate Difficulty)
    P2) Sum and Product List (Hard Difficulty)
    P3) 1D Array (Intermediate Difficulty)
    P4) Hard Difficulty
"""

from typing import List

#==============================================================================================
"""
Problem 1: Combine Two List (Intermediate Difficulty)
    1) Create two lists:
        a. list1 containing the integers from 1 to 10.
        b. list2 containing the cubes of integers from 1 to 10.

    2) Combine the two lits into a single list where:
        a. All elements of list1 come first, followed by all elements of list2.

    3) Count how many elemetns in the combined list are greater than 50.
"""

print("==============================================================================")

def combineList(list1: List[int], list2: List[int]) -> List[int]:
    return list1 + list2

def counter(comList: List[int]) -> int:
    count: int = 0
    for num in comList:
        if (num > 50):
            count += 1
    return count

"""
#** Test cases
"""
print("Question 1:")
list1: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(list2)):
    list2[i] = pow(list2[i], 3)

list3: List[int] = combineList(list1, list2)
print(list3)
print(f'Count of Elements > 50: {counter(list3)}')

print("==============================================================================")

#==============================================================================================
"""
Problem 2: Sum and Product List (Hard Difficulty)
    1) Ask the user to input two lists of size 5, where each list contains integers.

    2) Write a program to:
        a. Add the corresponding elemetns of the two lists and store the result1
           in a new list.
        b. Multiply the corresponding elements of the two lists and store the result in
           another new list.

    3) Print all three lists (original lists and the results).
"""

def prompt_input(position: int) -> List[int]:
    print(f"Enter 5 integers for list{position} (space-separated): ", end="")
    inputs = input().split()
    return [int(num) for num in inputs]

def sum_element(list1: List[int], list2: List[int]) -> List[int]:
    return [list1[i] + list2[i] for i in range(5)]

def multiply_element(list1: List[int], list2: List[int]) -> List[int]:
    return [list1[i] * list2[i] for i in range(5)]

"""
#** Test cases
"""
print("Question 2:")
arr1: List[int] = prompt_input(1)
arr2: List[int] = prompt_input(2)

print(f"List1: {arr1}")
print(f"List2: {arr2}")
print(f'Sum List: {sum_element(arr1, arr2)}')
print(f'Product List: {multiply_element(arr1, arr2)}')

print("==============================================================================")

#==============================================================================================
"""
Problem 3: 1D Array (Intermediate Difficulty)
    1) Create a 1D array of size 8, where each element is input by the user.

    2) Write a program to:
        a. Find and print all the even numbers in the array.
        b. Find and print the sum of all odd numbers in the array.
"""

def Array1D() -> List[int]:
    print(f'Enter 8 integers: ', end="")
    return [int(num) for num in input().split()]

def findEvenNumber(list1: List[int]) -> List[int]:
    return [num for num in list1 if num % 2 == 0]

def sum_odd_element(list1: List[int]) -> int:
    return sum([num for num in list1 if num % 2 != 0])

"""
#** Test cases
"""
print("Question 3:")
array1: List[int] = Array1D()
print(f"Even Numbers: {findEvenNumber(array1)}")
print(f"Sum of Odd Numbers: {sum_odd_element(array1)}")

print("==============================================================================")

#==============================================================================================
"""
Problem 4: Difference of two lists (Hard Difficulty)
    1) Create two arrays (array1 and array 2) of size 6, with each element entered by the user.

    2) Write a program to:
        a. Create a new array that contains the difference between corresponding elements of
           array1 and array2.
        b. Count how many elements in the difference array are negative.

    3) Print array1, array2, the difference array, and the count of negative elements,
"""

def generate_array_size_6(array_num: int) -> List[int]:
    print(f"Enter 6 integers for array{array_num}: ", end="")
    return [int(num) for num in input().split()]

def diff_arrays(list1: List[int], list2: List[int]) -> List[int]:
    return [list1[i] - list2[i] for i in range(6)]

def count_neg(list: List[int]) -> int:
    return len([num for num in list if num < 0])

"""
#** Test cases
"""
print("Question 4:")
Array1: List[int] = generate_array_size_6(1)
Array2: List[int] = generate_array_size_6(2)
print(f"Array1: {Array1}")
print(f"Array2: {Array2}")
diff_arr: List[int] = diff_arrays(Array1, Array2)
print(f"Difference Array: {diff_arr}")
print(f"Count of Negative Elements: {count_neg(diff_arr)}")

print("==============================================================================")

#==============================================================================================
