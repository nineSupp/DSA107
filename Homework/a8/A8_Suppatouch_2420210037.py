"""
Assignment 8: Tournament Results Sorting System

Name: Suppatouch Srinual
ID: 2420210037
"""
#==============================================================================================================================
"""
Problem Description
You are developing a system for an international gaming tournament. Each play has the following
instruction:
    - Player ID (String)
    - Username (String)
    - Score (Integer)
    - Win Rate (float, 0 - 100)
    - Country Code (String, 2 characters)

Task Requirements
Create a program that implements the following requirements:
    1. Create a sorting system that can:
        a, Sort players by score (primary).
        b, If scores are equal, sort by win rate (secondary).
        c. If both are equal, sort by username alphabetically (tertiary).

    2. The program must:
        a. Cannot use any built-in python sorting functions.
        b. Implement at least 2 different soorting algorithms of your choice.
        c. Allow users to choose which sorting algorithms of your choice.
        d. Display the sorting process step by step.

    3. Additional Features:
        a. Group players by country after sorting.
        b. Calculate average score per country.
        c. Find the median score per country.

Input Format
Example:
    players = [
        {'id': 'P123', 'username': 'DragonMaster', 'score': 2800, 'win_rate': 75.5, 'country': 'US'},
        {'id': 'P456', 'username': 'NinjaCoder', 'score': 2800, 'win_rate': 75.5, 'country': 'JP'},
        {'id': 'P789', 'username': 'CyberKnight', 'score': 2800, 'win_rate': 80.0, 'country': 'US'},
        {'id': 'P234', 'username': 'PixelWarrior', 'score': 2750, 'win_rate': 82.5, 'country': 'KR'},
        {'id': 'P567', 'username': 'BinaryBeast', 'score': 2900, 'win_rate': 70.0, 'country': 'JR'}
    ]

Required Output
    1. Sorted player list showing:
        Sorting Process:
        Step 1: [Current state of array]
        Stap 2: [Current state of array]
        ...

        Final Sorted Result:
        1. BinaryBeast (JP) - 2900 pts, 70.0%
        2. CyberKnight (US) - 2800 pts, 80.0%
        3. DragonMaster (US) - 2800 pts, 75.5%
        4. NinjaCoder (JP) - 2800 pts, 75.5%
        5. PixelWarrior (KR) - 2750 pts, 82.5%
        ...

    2. Country Statistics:
        Country Analysis:
        JP: Average Score: 2850, Median Score: 2850
        US: Average Score: 2800, Median Score: 2800
        KR: Average Score: 2750, Median ScoreL 2750

Implementation Requirements
    1. Create a Player class to store player informations.
    2. Implement custom comparison functions.
    3. Implement at least 2 sorting algorithms.
    4. Create functions for statistical calculations.
    5. Include step-by-step visualization.
    6. Handle all edge cases.

Sample Test Cases test_cases = [ 
    # Test Case 1: Same scores, different win rates 
    [ 
        {"id": "P1", "username": "Alpha", "score": 1000, "win_rate": 60.0, "country": "US"}, 
        {"id": "P2", "username": "Beta", "score": 1000, "win_rate": 70.0, "country": "US"} 
    ], 
     
    # Test Case 2: Same scores and win rates 
    [ 
        {"id": "P3", "username": "Charlie", "score": 1500, "win_rate": 80.0, "country": "JP"}, 
        {"id": "P4", "username": "Alpha", "score": 1500, "win_rate": 80.0, "country": "KR"} 
    ], 
     
    # Test Case 3: Mixed cases 
    [ 
        {"id": "P5", "username": "Delta", "score": 1200, "win_rate": 75.0, "country": "US"}, 
        {"id": "P6", "username": "Echo", "score": 1200, "win_rate": 75.0, "country": "JP"}, 
        {"id": "P7", "username": "Alpha", "score": 1200, "win_rate": 75.0, "country": "KR"} 
    ] 

"""
#==============================================================================================================================

from typing import List
from typing import Dict
import numpy as np
import time


class Player:
    def __init__(self, id: str, username: str, score: int, win_rate: float, country: str) -> None:
        self.id: str = id
        self.username: str = username
        self.score: int = score
        self.win_rate: float = win_rate
        self.country: str = country

    def __str__(self) -> str:
        return f'("id": {self.id}, "username": {self.username}, "score": {self.score}, "win_rate": {self.win_rate}, "country": {self.country})'
    
    def __repr__(self) -> str:
        return f'("id": {self.id}, "username": {self.username}, "score": {self.score}, "win_rate": {self.win_rate}, "country": {self.country})'

class Visualizing:
    @staticmethod
    def pretty_lst(lst: List[Player], highlight_indices=None) -> None:
        output: str = "[\n"
        for i, player in enumerate(lst):
            if highlight_indices and i in highlight_indices:
                output += f"\t!{player}!\n"
            else:
                output += f"\t {player}\n"
        output += "]"
        return output

    def show_step(self, step: int, players: List[Player], action: str, indices=None):
        print(f"Step {step}: {action}")
        print(self.pretty_lst(players, highlight_indices=indices))
        print("=" * 100)

    def show_summary(self, sorting_type: str, before: List[Player], after: List[Player], time_taken: float):
        print(f"Final Result ({sorting_type}):")
        print(f"Time Taken: {time_taken:.6f} seconds")
        print("Before Sorting:")
        print(self.pretty_lst(before))
        print("After Sorting:")
        print(self.pretty_lst(after))

    def show_final_result(self, lst: List[Player]) -> None:
        print("=" * 100)
        print("Final Sorted Result:")
        for i in range(len(lst)):
            print(f"{i + 1}. {lst[i].username} ({lst[i].country}) - {lst[i].score} pts, {lst[i].win_rate}%")

    def country_analysis(self, lst: List[Player]) -> None:
        print("=" * 100)
        print("Country Analysis:")
        total_score: List[int] = []
        dict_country: Dict[str, List[int]] = {}
        for i in range(len(lst)):
            if lst[i].country in dict_country.keys():
                dict_country[lst[i].country].append(lst[i].score)
            else:
                dict_country.update({lst[i].country : [lst[i].score]})
            total_score.append(lst[i].score)

        for country, scores in dict_country.items():
            print(f"{country}: Average Score: {round(np.mean(scores))}, Median Score: {round(np.median(scores))}")

class SortingTournament:
    def __init__(self, players: List[Dict]):
        self.players = [Player(**player) for player in players]
        self.original_players = self.players[:]
        self.stats = {"steps": 1, "comparisons": 0, "swaps": 0}
        self.visualizer = Visualizing()
        self.ask_sort()

    def ask_sort(self):
        print("=" * 100)
        print("Choose sorting method:")
        print("1. Selection Sort")
        print("2. Bubble Sort")
        choice = input("Enter choice (1/2): ")
        if choice == "1":
            self.selection_sort()
        elif choice == "2":
            self.bubble_sort()
        else:
            print("Invalid choice. Try again.")
            self.ask_sort()
        print("=" * 100)

    def selection_sort(self):
        print("=" * 100)
        print("Selection Sort:")
        start_time = time.time()
        for i in range(len(self.players)):
            min_index = i
            for j in range(i + 1, len(self.players)):
                self.stats["comparisons"] += 1
                if self.compare(self.players[j], self.players[min_index]):
                    min_index = j
            self.swap(i, min_index)
        time_taken = time.time() - start_time
        self.visualizer.show_summary("Selection Sort", self.original_players, self.players, time_taken)
        self.visualizer.show_final_result(self.players)
        self.visualizer.country_analysis(self.players)

    def bubble_sort(self):
        print("=" * 100)
        print("Bubble Sort")
        start_time = time.time()
        for i in range(len(self.players) - 1):
            swapped = False
            for j in range(len(self.players) - 1 - i):
                self.stats["comparisons"] += 1
                if self.compare(self.players[j + 1], self.players[j]):
                    self.swap(j, j + 1)
                    swapped = True
            if not swapped:
                break
        time_taken = time.time() - start_time
        self.visualizer.show_summary("Bubble Sort", self.original_players, self.players, time_taken)
        self.visualizer.show_final_result(self.players)
        self.visualizer.country_analysis(self.players)

    def compare(self, player1: Player, player2: Player) -> bool:
        if player1.score != player2.score:
            return player1.score > player2.score
        if player1.win_rate != player2.win_rate:
            return player1.win_rate > player2.win_rate
        return player1.username < player2.username

    def swap(self, i: int, j: int):
        if i != j:
            self.stats["swaps"] += 1
            self.visualizer.show_step(self.stats["steps"], self.players, f"Swapping indices {i} and {j}", indices=[i, j])
            self.players[i], self.players[j] = self.players[j], self.players[i]
            self.stats["steps"] += 1

#==============================================================================================================================
# Test Case 1: Same scores, different win rates.
players1: List[dict[str, int] | dict[str, str] | dict[str, float]] = [
        {"id": "P1", "username": "Alpha", "score": 1000, "win_rate": 60.0, "country": "US"}, 
        {"id": "P2", "username": "Beta", "score": 1000, "win_rate": 70.0, "country": "US"}
]
st1: SortingTournament = SortingTournament(players1)


# Test Case 2: Same scores and win rates.
players2: List[dict[str, int] | dict[str, str] | dict[str, float]] = [
        {"id": "P3", "username": "Charlie", "score": 1500, "win_rate": 80.0, "country": "JP"}, 
        {"id": "P4", "username": "Alpha", "score": 1500, "win_rate": 80.0, "country": "KR"}
]
st2: SortingTournament = SortingTournament(players2)

# Test Case 3: Mixed cases
players3: List[dict[str, int] | dict[str, str] | dict[str, float]] = [ 
        {"id": "P5", "username": "Delta", "score": 1200, "win_rate": 75.0, "country": "US"}, 
        {"id": "P6", "username": "Echo", "score": 1200, "win_rate": 75.0, "country": "JP"}, 
        {"id": "P7", "username": "Alpha", "score": 1200, "win_rate": 75.0, "country": "KR"} 
    ]

st3: SortingTournament = SortingTournament(players3)

#==============================================================================================================================
