"""
Assignment 7: Bubble Sort

Name: Suppatouch Srinual
ID: 2420210037
"""
#==============================================================================================
"""
Objective
 - Create an interactive visualization system that shows how Bubble Sort works step by step.

Requirement
    1. User Input Features
        a. Let users:
            a.1) Enter their own numbers.
            a.2) Generate random numbers.
            a.3) Choose how many numbers (max 100).
            a,4) Control sorting speed.

    2. Visual Display
        b. Show:
            b,1) Current state of numbers.
            b.2) Which numbers are being compared.
            b.3) Swapping animation.
            b.4) Which part is already sorted.
            b.5) Which pass number we're on.
            b.6) How far along we are.

    3. Basic Metrics
        c. Count and show:
            c.1) How many comparisons made.
            c.2) How many swaps done.
            c.3) How long it took.
            c.4) Current progress percentage.

    Example Output:
        Numbers now: [5, 3, 8, 4, 2]
        Step 1: Looking at 5 and 3
        [5*, 3*, 8, 4, 2] -> Need to swap
        [3, 5, 8, 4, 2] -> After swap
        -------------------------------------
        Stats:
        - Compared: 1 times
        - Swapped: 1 times
        - Time: 0.001s
        Done: 5%
"""

#===========================================================================================================

from typing import List
import random as rd
import time


class BubbleSortVisualizer:
    def __init__(self) -> None:
        self.numbers: List[int] = []
        self.tempNums: List[int] = []

        self.comparisons: int = 0
        self.swaps: int = 0
        self.time_taken: float = 0.0
        self.current_steps: int = 1
        self.total_comparison: int = 0
    
    """ Generate random numbers """
    def get_random_numbers(self, size: int) -> None:
        if size < 0:
            print("The input size is less than 0. Please put a new size >= 0.")
        elif size > 100:
            print("The input size exceed the maximum range 100. Please put a new size.")
        else:
            for _ in range(size):
                self.numbers.append(rd.randint(1, 10))
        self.tempNums: List[int] = self.numbers[:]

    """ Use numbers from user """
    def set_user_numbers(self, numbers) -> None:
        self.numbers = numbers
        self.tempNums: List[int] = self.numbers[:]

    """ Bubble Sort """
    def do_sorting(self) -> None:
        array_length: int = len(self.numbers)
        self.total_comparison = (array_length * (array_length - 1)) // 2
        start: time = time.time()

        for i in range(array_length):
            is_swapped: bool = False
            for j in range(array_length - 1 - i):
                self.show_current_step(self.numbers[j], self.numbers[j + 1])
                self.comparisons += 1
                
                if self.numbers[j] > self.numbers[j + 1]:
                    self.animate_swap(j, j + 1)

                    temp: int = self.numbers[j]
                    self.numbers[j] = self.numbers[j + 1]
                    self.numbers[j + 1] = temp
                    is_swapped = True
                    self.swaps += 1

                    print(f"{self.numbers} -> After swap")
                    print("-" * (len(self.numbers) * 5))

                    self.current_steps += 1

                else:
                    print("No swap!")
                    print("-" * (len(self.numbers) * 5))
                    self.current_steps += 1

                self.time_taken = time.time() - start
                self.show_stats()

            if not is_swapped:
                break

        self.complete()

    """ Show step """
    def show_current_step(self, pos1: int, pos2: int) -> None:
        print("=" * (len(self.numbers) * 5))
        print(f"Numbers now: {self.numbers}")
        print(f"Step {self.current_steps}: Looking at {pos1} and {pos2}")

    """ Show stats """
    def show_stats(self) -> None:
        print(f"Stats:")
        print(f"- Compared: {self.comparisons} times")
        print(f"- Swapped: {self.swaps} times")
        print(f"- Time: {self.time_taken:.3f}s")
        print(f"Done: {int((self.comparisons / self.total_comparison) * 100)}%")
        print("=" * (len(self.numbers) * 10))

    """ Animation """
    def animate_swap(self, pos1: int, pos2: int) -> None:
        copy_arr: List[int] = self.numbers[:]
        copy_arr[pos1], copy_arr[pos2] = f"{self.numbers[pos2]}*", f"{self.numbers[pos1]}*"
        print(f"{copy_arr} -> Need to swap")

    def complete(self):
        print("=" * (len(self.numbers) * 10))
        print("Sorting Complete!")
        print(f"Old array: {self.tempNums}")
        print(f"Sorted array: {self.numbers}")
        print("=" * (len(self.numbers) * 10))

#===========================================================================================================
# Test case 1

lst: List[int] = [5, 3, 8, 4, 2]
bbs1: BubbleSortVisualizer = BubbleSortVisualizer()
bbs1.set_user_numbers(lst)
bbs1.do_sorting()


# Test case 2
# bbs1.get_random_numbers(10)
print(bbs1.numbers)
bbs1.do_sorting()
