"""
Assignment 7A: Selection Sort

Name: Suppatouch Srinual
ID: 2420210037
"""
#==============================================================================================
"""
Problem Description
    You are tasked with creating a student performance analysis system for a school. The system
    should sort and analyze student records using the Selection Sort algorithm.

Requirements
    1. Create Student Class
        def Student:
            def __init__(self, id, name, score, attendence):
                self.id = id                    # Student ID (string)
                self.name = name                # Student name (string)
                self.score = score              # Test score (float)
                self.attendance = attendance    # Attendance percentage (float)

    2. Implement Modified Selection Sort
        Your task is to implement a Selection Sort that can:
            a. Sort students by different criteria (score, attendance, name).
            b. Sort in both ascending and descending order.
            c. Track and display the sorting process.
            d. Count comparisons and swaps.

                def selection_sort(students, sort_by, order="ascending'):
                    '''
                    Sort student records using selection sort

                    Parameters:
                    student: List of Student objects
                    sort_by: 'score', 'attendance', or 'name'
                    order: 'ascending' or 'descending'

                    Returns:
                    sorted_students: Sorted list of Student object.
                    stats: Dictionary containing number of compairsons and swaps
                    '''

    3. Required Functions
        def selection_sort_students(students, sort_by, order='ascending'):
            '''
            Sort student records using selection sort

            Parameters:
            student: List of Student objects
            sort_by: 'score', 'attendance', or 'name'
            order: 'ascending' or 'descending'

            Returns:
            sorted_students: Sorted list of Student object.
            stats: Dictionary containing number of compairsons and swaps
             '''

    4. Specific Tasks
        1. Basic Implementation:
            a. Implement Selection Sort for the Student class.
            b. Add visualization of each step.
            c. Count and display operations.

        2. Multiple Sorting Criteria:
            a. Score (highest to lowest).
            b. Attendance (highest to lowest).
            c. Name (alphabetical order).

    5. Example Test Data
        test_data = [
            Student("A001", "John", 85.5, 92.0),
            Student("A002", "Alice", 92.0, 88.5),
            Student("A003", "Bob", 78.5, 95.0),
            Student("A004", "Mary", 90.0, 91.5),
            Student("A005", "David", 88.0, 05.0)
        ]

"""

#===========================================================================================================

from typing import List
import time


class Student:
    def __init__(self, id: str, name: str, score: float, attendance: float) -> None:
        self.id = id
        self.name = name
        self.score = score
        self.attendance = attendance

    def __str__(self):
        return f'Student(ID: {self.id}, Name: {self.name}, Score: {self.score}, Attendance: {self.attendance})'

    def __repr__(self):
        return f'Student(ID: {self.id}, Name: {self.name}, Score: {self.score}, Attendance: {self.attendance})'

class Selection_Sort:
    def __init__(self):
        # compaisons and swaps
        self.original: List[Student] = []
        self.stats: dict[int, int] = {"comparisons" : 0, "swaps" : 0}
        self.steps: int = 1
        pass

    def selection_sort_students(self, students: List[Student], sort_by: str, order: str) -> List[Student]:
        # Base cases
        if len(students) == 0:
            print("len students == 0!")
            return students
        
        if sort_by.lower() not in ['score', 'name', 'attenance']:
            print("Unknown sort-by!")
            return students
        
        if order.lower() not in ['ascending', 'descending']:
            print("Unknown order!")
            return students

        self.original = students[:]
        start: float = time.time()
        total_comparison: int = (len(students) * (len(students) - 1)) // 2
        for i in range(len(students)):
            currentDex: int = i
            for j in range(i + 1, len(students)):
                self.steps += 1
                self.stats["comparisons"] += 1
                if self.get_value_students(students[j], students[currentDex], sort_by, order):
                    currentDex = j
            if currentDex != i:
                self.visualize(students, j, currentDex, True)
                temp: Student = students[i]
                students[i] = students[currentDex]
                students[currentDex] = temp
                self.stats['swaps'] += 1
                self.print_stats(students, time.time() - start, total_comparison)
            else:
                self.visualize(students, j, currentDex, False)
                self.print_stats(students, time.time() - start, total_comparison)

        end: float = time.time()
        self.complete(students, end - start)
        return students

    def get_value_students(self, next_student: Student, current_student: Student, sort_by: str, order: str) -> bool:
        if sort_by.lower() == 'score':
            n_student_value = next_student.score
            c_student_value = current_student.score
        elif sort_by.lower() == 'name':
            n_student_value = next_student.name
            c_student_value = current_student.name
        elif sort_by.lower() == 'attendance':
            n_student_value = next_student.attendance
            c_student_value = current_student.attendance
        else:
            return False
        
        return self.compare_value(n_student_value, c_student_value, order)

    def compare_value(self, n_student_value, c_student_value, order: str) -> bool:
        if order.lower() == 'ascending':
            return n_student_value < c_student_value
        elif order.lower() == 'descending':
            return n_student_value > c_student_value
        return False

    def pretty_list(self, arr: List[Student]) -> str:
        pretty: str = "["
        for i in range(len(arr)):
            if i == len(arr) - 1:
                pretty += "\t  " + str(arr[i])
            elif i == 0:
                pretty += " " + str(arr[i]) + ",\n"
            else:
                pretty += "\t  " + str(arr[i]) + ",\n"
        return pretty + "\n\t]"

    def visualize(self, students: List[Student], pos1: int, pos2: int, is_swapped: bool) -> None:
        print("=" * (len(students) * 20))

        print(f"Current Array: {self.pretty_list(students)}\n")
        print(f"Steps {self.steps}: Looking at **{students[pos1]}** and **{students[pos2]}**")
        
        if is_swapped:
            copy_arr = students[:]
            copy_arr[pos1], copy_arr[pos2] = f'**{copy_arr[pos1]}**', f"**{copy_arr[pos2]}**"
            print(f"Need to swap: {self.pretty_list(copy_arr)}")
            temp = students[:]
            temp[pos1], temp[pos2] = f"{temp[pos2]}", f"**{temp[pos1]}"
            print(f"{self.pretty_list(temp)}\n")
        else:
            print("No swap!")
            print(f"Current Array: {self.pretty_list(students)}\n")

    def print_stats(self, students: List[Student], time_taken: float, total_comparison: int) -> None:
        print("-" * (len(students) * 20))
        print("Stats:")
        print(f"- Compared: {self.stats["comparisons"]} times")
        print(f"- Swapped: {self.stats["swaps"]} times")
        print(f"- Time: {time_taken:.3f}s")
        print(f"Done: {int((self.stats['comparisons'] / total_comparison) * 100)}%")
        print("=" * (len(students) * 20))

    def complete(self, students: List[Student], total_time: float) -> None:
        print("=" * (len(students) * 20))
        print("Selection Sort Complete!")
        print(f"Old array: {self.pretty_list(self.original)}")
        print(f"Sorted array: {self.pretty_list(students)}")
        print(f"- Total Time Taken: {total_time:.3f}s")
        print("=" * (len(students) * 20))
        pass
#===========================================================================================================
# Test case 1

test_data: List[Student] = [
            Student("A001", "John", 85.5, 92.0),
            Student("A002", "Alice", 92.0, 88.5),
            Student("A003", "Bob", 78.5, 95.0),
            Student("A004", "Mary", 90.0, 91.5),
            Student("A005", "David", 88.0, 05.0)
        ]

ss1: Selection_Sort = Selection_Sort()
a = ss1.selection_sort_students(test_data[:], 'name', 'ascending')
# print(a)
