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
    def pretty_lst(self, lst: List[Player]) -> str:
        pretty_lst: str = '['
        for i in range(len(lst)):
            if i == len(lst) - 1:
                pretty_lst += "\t" + str(lst[i])
            elif i == 0:
                pretty_lst += " " + str(lst[i]) + ",\n"
            else:
                pretty_lst += "\t " + str(lst[i]) + ",\n"
        return pretty_lst + "\n\t]"

    def sort_process(self, step: int, current_state: List[Player], is_swapped: bool, i: int, j: int) -> None:
        if is_swapped:
            self.print_line(step, current_state, 'Swap', i, j)
        else:
            self.print_line(step, current_state, 'No Swap', i, j)

    def complete(self, type_sort: str, before_lst: List[Player], after_lst: List[Player], time_taken: float) -> None:
        print(f"Final Result for {type_sort}:")
        print(f"Total time taken: {time_taken:.6f}s")
        print(f'Before {type_sort}:')
        print(f'{self.pretty_lst(before_lst)}')
        print(f'After {type_sort}:')
        print(f'{self.pretty_lst(after_lst)}')
        print("=" * 100)

    def print_line(self, step: int, current_state: List[Player], swap: str, i: int, j: int) -> None:
        print(f'Steps: {step}: {swap}!')
        print(f'Looking at index: {i} and {j}')
        # Animate...
        self.animate_swap()

        print(f'{self.pretty_lst(current_state)}')
        print("=" * 100)

    def animate_swap(self) -> None:

class SortingTournament:
    def __init__(self, players: List[dict[str, int] | dict[str, str] | dict[str, float]]) -> None:
        self.lst_players: List[Player] = self.get_players(players)
        self.original: List[Player] = self.lst_players[:]
        self.select_stats: dict[str, int] = {"steps": 1, "comparisons": 0, 'swaps': 0}
        self.visual: Visualizing = Visualizing()

    def get_players(self, players: List[dict[str, int] | dict[str, str] | dict[str, float]]) -> List[Player]:
        changed_lst: List[Player] = []

        for player in players:
            changed_lst.append(Player(player["id"], player['username'], player['score'], player['win_rate'], player['country']))

        return changed_lst

    def do_compare(self, sort_by: str, player1: Player, player2: Player) -> bool:
        if sort_by.lower() == 'score':
            p1_val: int = player1.score
            p2_val: int = player2.score
            if self.is_equal(p1_val, p2_val):
                return self.do_compare('win_rate', player1, player2)
            return self.compairing(p1_val, p2_val)

        elif sort_by.lower() == 'win_rate':
            p1_val: float = player1.win_rate
            p2_val: float = player2.win_rate
            if self.is_equal(p1_val, p2_val):
                return self.do_compare('username', player1, player2)
            return self.compairing(p1_val, p2_val)

        elif sort_by.lower() == 'username':
            p1_val: str = player1.username
            p2_val: str = player2.username
            return self.compairing(p1_val, p2_val)
        else:
            return False

    def is_equal(self, val1: int | float | str, val2: int | float | str) -> bool:
        return val1 == val2

    def compairing(self, p1_value: int | float | str, p2_value: int | float | str) -> bool:
        return p2_value > p1_value

    def selection_sort(self) -> List[Player]:
        if len(self.lst_players) <= 0:
            print("len student == 0.")
            return self.lst_players

        print("=" * 100)
        print("Selection Sort Process:")
        start: float = time.time()
        for i in range(len(self.lst_players)):
            currentDex: int = i
            for j in range(i + 1, len(self.lst_players)):
                if self.do_compare('score', self.lst_players[j], self.lst_players[currentDex]):
                    self.select_stats['comparisons'] += 1
                    currentDex = j

            self.do_swap(i, currentDex)
            self.select_stats['steps'] += 1
    
        end: float = time.time()
        self.visual.complete('Selection Sort', self.original, self.lst_players, end - start)
        return self.lst_players

    def do_swap(self, i: int, currentDex: int) -> bool:
        if currentDex != i:
            temp: Player = self.lst_players[i]
            self.lst_players[i] = self.lst_players[currentDex]
            self.lst_players[currentDex] = temp
            self.select_stats['swaps'] += 1
            self.visual.sort_process(self.select_stats['steps'], self.lst_players, True, i, currentDex)
        else:
            self.visual.sort_process(self.select_stats['steps'], self.lst_players, False, i, currentDex)

#==============================================================================================================================
players: List[dict[str, int] | dict[str, str] | dict[str, float]] = [ 
        {"id": "P5", "username": "Delta", "score": 1200, "win_rate": 75.0, "country": "US"}, 
        {"id": "P6", "username": "Echo", "score": 1200, "win_rate": 75.0, "country": "JP"}, 
        {"id": "P7", "username": "Alpha", "score": 1200, "win_rate": 75.0, "country": "KR"} 
    ]

st1: SortingTournament = SortingTournament(players)
st1.selection_sort()

#==============================================================================================================================