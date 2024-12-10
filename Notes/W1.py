"""
Week 1: Recursion

Name: Suppatouch Srinual
ID: 2420210037
"""

import time


# Example of using recursion for sum from 1 to n.
def sum_recursive(n: int) -> int:
    # Base case
    if (n == 1):
        return 1
    else:
        # Recursive case
        return sum_recursive(n - 1) + n

# print(sum_recursive(5))

# Example of using recursion for factorial.
def fac_recursive(n: int) -> int:
    if (n == 0):
        return 1
    else:
        return fac_recursive(n - 1) * n

# print(fac_recursive(5))


# Example of using recursion for fibonacci.
# n = position of fibonacci sequence.
def fib_recursive(n: int) -> int:
    if (n == 0): 
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

start = time.time()
print(fib_recursive(38))
end = time.time()
print(end - start)


## Stack
# (Interupt hold the program).
## First In Last Out (FILO)
## Last In First Out (LIFO)
### First In First Out (FIFO)
