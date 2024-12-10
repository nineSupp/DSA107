"""
Assignment 1

Name: Suppatouch Srinual
ID: 2420210037

# Instructions:
# 1) Write each program in Python using recursion.
# 2) Include a base case and recursive case in every program.
# 3) Test your code with various inputs.
"""

from typing import List


#======================================================================================
#** Question 1: Sum of Odd Numbers from 1 to N.
#* Write a recursive function to calculate the sum of all odd numbers from 1 to N.
#*
#* Example:
#* Input: n = 7
#* Output: 16

## This will print the total sum.
def sum_odd_recur(n: int) -> int:
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        if (n % 2 != 0):
            return n + sum_odd_recur(n - 1)
        else:
            return sum_odd_recur(n - 1)

"""
Test cases:
"""
print("Test cases Q1:")
print(sum_odd_recur(-20))
print(sum_odd_recur(0))
print(sum_odd_recur(1))
print(sum_odd_recur(7))
print(sum_odd_recur(33))
print(sum_odd_recur(423))


## This will print the sequence of sum of odd numbers: 1 + 3 + 5 + 7 = 16
# def sum_odd_recur_print(n: int) -> int:

"""
Test cases:
"""
# print(GCD(48, 18))
# print(GCD(0, 0))
# print(GCD(12, 30))
# print(GCD(123, 36))
# print(GCD(14, 22))

print()

#======================================================================================
#** Question 2: Reverse a String.
#* Write a recursive function to reverse a given string.
#*
#* Example:
#* Input: "arun"
#* Output: "nura"

def reverse_string_recur(input: str) -> str:
    if (len(input) == 0):
        return ""
    elif (len(input) == 1):
        return input[0]
    else:
        reverse: str = input[len(input) - 1] + reverse_string_recur(input[: len(input) - 1])
        return reverse

"""
Test cases:
"""
print("Test cases Q2:")
print(reverse_string_recur("arun"))
print(reverse_string_recur("Lorem ipsum"))
print(reverse_string_recur("banana"))
print(reverse_string_recur("DaTa StRuCtUrE aNd AlGoRiThMs"))
print(reverse_string_recur("HelloWorld"))

print()

#======================================================================================
#** Question 3: Find the Greatest Common Divisor (GCD).
#* Write a recursive function to find the GCD of two integers using the Euclidean
#* algorithm,
#*
#* Example:
#* Input: a = 48, b = 18
#* Output: GCD = 6

def GCD(a: int, b:int) -> int:
    if (abs(a) == 0 or abs(b) == 0):
        return 0
    elif (abs(a) > abs(b)):
        if (abs(a) % abs(b) == 0):
            return abs(b)
        else:
            return GCD(abs(b), abs(a) % abs(b))
    else:
        if (abs(b) % abs(a)  == 0):
            return abs(a)
        else:
            return GCD(abs(a), abs(b) % abs(a))

"""
Test cases:
"""
print("Test cases Q3:")
print(GCD(48, 18))
print(GCD(0, 0))
print(GCD(12, 30))
print(GCD(123, 36))
print(GCD(26, 15))

print()

#======================================================================================
#** Question 4: Count Vowels in a String.
#* Write a recursive function to count the number of vowels in a given string.
#*
#* Example:
#* Input: "hello"
#* Output: 2 (vowels: e, o)

def count_vowels(input: str) -> int:
    if (len(input) == 0):
        return 0
    else:
        input = input.lower()
        if ("a" in input[-1] or "e" in input[-1] or "i" in input[-1] or "o" in input[-1] or 
            "u" in input[-1]):
            return 1 + count_vowels(input[: len(input) - 1])
        else:
            return count_vowels(input[: len(input) - 1])

"""
Test cases:
"""
print("Test cases Q4:")
print(count_vowels("hello"))
print(count_vowels("aeiou"))
print(count_vowels("aatto"))
print(count_vowels("abcdefghijklmnopqrstuvwxyz"))
print(count_vowels("data structureiiii"))

print()

#======================================================================================
#** Question 5: Exponentiation.
#* Write a recursive function to calculate a^b (a raised to the power of b).
#*
#* Example:
#* Input: a = 2, b = 4
#* Output: 16

def exponential(a: int, b: int) -> int:
    if (b == 0 or a == 0):
        return 1
    elif (b == 1):
        return a
    else:
        return a * exponential(a, b - 1)

"""
Test cases:
"""
print("Test cases Q5:")
print(exponential(2, 4))
print(exponential(10, 4))
print(exponential(2, 8))
print(exponential(2, 0))
print(exponential(3, 5))

print()

#======================================================================================
#** Question 6: Check if a String is a Palindrome.
#* Write a recursive function to check if a string is a palindrome (reads the same for
#* -ward and backward).
#* 
#* Example:
#* Input: "radar"
#* Output: True
#* [radar, level, madam, refer, civic, deified, racecar, rotor, noon, stats, etc.]
#* NOTE: BY DEFAULT A SINGLE CHARACTER IS A PALINDROME!

def palindrome(input: str) -> bool:
    if (len(input) <= 1):
        return True
    else:
        input = input.lower()
        input = input.replace(" ", "")
        if (input[0] == input[-1]):
            return palindrome(input[1 : len(input) - 1])
        else:
            return False

"""
Test cases:
"""
print("Test cases Q6:")
print(palindrome(""))
print(palindrome("radar"))
print(palindrome("racecar"))
print(palindrome("algorithms"))
print(palindrome("a"))
print()
 
#======================================================================================
#** Question 7: Count Occurences of a Character.
#* Write a recursive function to count the number of times a specific character appears
#* in strings.
#*
#* Example:
#* Input: "mississippi", "s"
#* Output: 4

def count_occurrences(input: str, ch: str) -> int:
    if (len(ch) == 0):
        return 0
    elif (len(input) <= 0):
        return 0
    else:
        if (input[:len(ch)] == ch):
            return 1 + count_occurrences(input[len(ch):], ch)
        else:
            return count_occurrences(input[len(ch):], ch)

"""
Test cases:
"""
print("Test cases Q7:")
print(count_occurrences("mississippi", "s"))
print(count_occurrences("thainichiinstituteoftechnology", "i"))
print(count_occurrences("thainichiinstituteoftechnology", "o"))
print(count_occurrences("thainichiinstituteoftechnology", "g"))
print(count_occurrences("thailand", "z"))

print()

#======================================================================================
#** Question 8: Generate All Subsets of a String
#* Write a recursive function to generate all subsets (or power sets) of a given string.
#* 
#* Example:
#* Input: "abc"
#* Output: ["", "a", "b", "c", "ab", "ac", "bc", "abc"]

def gen_subset(input: str) -> List[str]:
    def power_subset(input: str, dex: int, current: str) -> List[str]:
        if (dex == len(input)):
            return [current]
        else:
            return power_subset(input, dex + 1, current) + power_subset(input, dex + 1, current + input[dex])
    return sorted(list(set(power_subset(input, 0, ""))))

"""
Test cases:
"""
print("Test cases Q8:")
print(gen_subset("abc"))
print(gen_subset("123"))
print(gen_subset("fg"))
print(gen_subset("1234"))
print(gen_subset(""))
print()

#======================================================================================
#** Assertion and Test Case
# Question 1:
def assertQ1() -> None:
    assert sum_odd_recur(-300) == 0
    assert sum_odd_recur(0) == 0
    assert sum_odd_recur(4) == 4
    assert sum_odd_recur(3) == 4
    assert sum_odd_recur(60) == 900
    assert sum_odd_recur(423) == 44944
    print("ALL QUESTION 1 TEST PASSED!")

# Question 2:
def assert02() -> None:
    assert reverse_string_recur("") == ""
    assert reverse_string_recur("v") == "v"
    assert reverse_string_recur("TNIC") == "CINT"
    assert reverse_string_recur("Suppatouch Srinual") == "launirS hcuotappuS"
    assert reverse_string_recur("ViSuAl StUdIo CoDe") == "eDoC oIdUtS lAuSiV"
    assert reverse_string_recur("The length of this test case is exceedingly long, in order to test") == "tset ot redro ni ,gnol ylgnideecxe si esac tset siht fo htgnel ehT"
    print("ALL QUESTION 2 TEST PASSED!")

# Question 3:
def assert03() -> None:
    assert GCD(14, 28) == 14
    assert GCD(31, 17) == 1
    assert GCD(-10, -32) == 2
    assert GCD(56, 80) == 8
    assert GCD(60, 36) == 12
    assert GCD(-36, 60) == 12
    print("ALL QUESTION 3 TEST PASSED!")

# Question 4:,  
def assert04() -> None:
    assert count_vowels("") == 0
    assert count_vowels("COMPUTER") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("beautiful") == 5
    assert count_vowels("banana") == 3
    print("ALL QUESTION 4 TEST PASSED!")

# Question 5:
def assert05() -> None:
    assert exponential(0, 0) == 1
    assert exponential(2, 3) == 8
    assert exponential(5, 4) == 625
    assert exponential(3, 5) == 243
    assert exponential(10, 2) == 100
    assert exponential(7, 3) == 343
    print("ALL QUESTION 5 TEST PASSED!")

# Question 6:
def assert06() -> None:
    assert palindrome("") == True
    assert palindrome("c") == True
    assert palindrome("hello") == False
    assert palindrome("Gorilla") == False
    assert palindrome("A man a plan a canal Panama") == True
    assert palindrome("Able was I ere I saw Elba") == True
    print("ALL QUESTION 6 TEST PASSED!")

# Question 7:
def assert07() -> None:
    assert count_occurrences("", "a") == 0
    assert count_occurrences("banana", "a") == 3
    assert count_occurrences("taxi", "") == 0
    assert count_occurrences("aaaa", "a") == 4
    assert count_occurrences("aaaa", "aa") == 2 
    assert count_occurrences("Hello", "hello") == 0
    print("ALL QUESTION 7 TEST PASSED!")

# Question 8:
def assert08() -> None:
    assert gen_subset("") == sorted([""])
    assert gen_subset("a") == sorted(["", "a"])
    assert gen_subset("ab") == sorted(["", "a", "b", "ab"])
    assert gen_subset("abb") == sorted(["", "a", "b", "bb", "ab", "abb"])
    assert gen_subset("1234") == sorted(["", "1", "2", "3", "4", "12", "13", "14", "23", "24", "34", "123", "124", "134", "234", "1234"])
    assert gen_subset("car") == sorted(["", "c", "a", "r", "ca", "cr", "ar", "car"])
    print("ALL QUESTION 8 TEST PASSED!")

assertQ1()
assert02()
assert03()
assert04()
assert05()
assert06()
assert07()
assert08()

#======================================================================================
