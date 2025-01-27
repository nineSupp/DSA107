x : dict[str, int] = {"Nine": 2, "Pheem": 3, "Paing": 4}
print(x)

for i in x:
    print(i)


for i in x.values():
    print(i)


for i, j in x.items():
    print(i, j)

print(x["Pheem"])

x["Pheem"] += 1

print(x["Pheem"])


# class Visualizing:
#     def pretty_lst(self, lst: List[Player], is_swapped: bool, i: int, j: int) -> str:
#         if is_swapped:
#             pretty_lst: str = "["
#             for x in range(len(lst)):
#                 if (x == len(lst) -1):
#                     if x == i or x == j:
#                         pretty_lst += "!" + str(lst[x]) + "!"
#                     else:
#                         pretty_lst += "\t " + str(lst[x])
#                 elif x == 0:
#                     if x ==i or x == j:
#                         pretty_lst += "!" + str(lst[x]) + "!,\n"
#                     else:
#                         pretty_lst += "\t " + str(lst[i]) + ",\n"
#                 else:
#                     if x ==i or x == j:
#                         pretty_lst += "!" + str(lst[x]) + "!,\n"
#                     else:
#                         pretty_lst += "\t " + str(lst[i]) + ",\n"
#             return pretty_lst + "\n\t]"
#         else:
#             pretty_lst: str = '['
#             for i in range(len(lst)):
#                 if i == len(lst) - 1:
#                     pretty_lst += "\t " + str(lst[i])
#                 elif i == 0:
#                     pretty_lst += " " + str(lst[i]) + ",\n"
#                 else:
#                     pretty_lst += "\t " + str(lst[i]) + ",\n"
#             return pretty_lst + "\n\t]"

#     def complete(self, type_sort: str, before_lst: List[Player], after_lst: List[Player], time_taken: float) -> None:
#         print(f"Final Result for {type_sort}:")
#         print(f"Total time taken: {time_taken:.6f}s")
#         print(f'Before {type_sort}:')
#         print(f'{self.pretty_lst(before_lst, False, 0, 0)}')
#         print(f'After {type_sort}:')
#         print(f'{self.pretty_lst(after_lst, False, 0, 0)}')
#         print("=" * 100)

#     def before_swap(self, step: int, current_state: List[Player], swap: str, i: int, j: int, is_swapped: bool) -> None:
#         print(f'Steps {step}: {swap}!')
#         print(f'Looking at index: {i} and {j}')
#         print(f"Before swap:")
#         print(f'{self.pretty_lst(current_state, is_swapped, i, j)}')

#     def after_swap(self, current_state: List[Player], is_swapped: bool) -> None:
#         print(f"After swaps:")
#         print(f'{self.pretty_lst(current_state, is_swapped, 0, 0)}')
#         print("=" * 100)

# class SortingTournament:
#     def __init__(self, players: List[dict[str, int] | dict[str, str] | dict[str, float]]) -> None:
#         self.lst_players: List[Player] = self.get_players(players)
#         self.original: List[Player] = self.lst_players[:]
#         self.stats: dict[str, int] = {"steps": 1, "comparisons": 0, 'swaps': 0}
#         self.visual: Visualizing = Visualizing()
#         self.ask_sort()

#     def ask_sort(self) -> None:
#         print('=' * 100)
#         print("Choose the sorting process: ")
#         print("1. Selection Sort")
#         print("2. Bubble Sort")
#         get_val: str = input("Enter the input: ")
#         self.select_process(get_val)

#     def select_process(self, value: str) -> None:
#         if value in ['1', '2', 'Selection Sort', 'Bubble Sort']:
#             if value == '1' or value == "Selection Sort":
#                 self.selection_sort()
#             else:
#                 self.bubble_sort()
#         else:
#             print("Unknown Input please try to enter the input again.")
#             self.ask_sort()

#     def get_players(self, players: List[dict[str, int] | dict[str, str] | dict[str, float]]) -> List[Player]:
#         changed_lst: List[Player] = []

#         for player in players:
#             changed_lst.append(Player(player["id"], player['username'], player['score'], player['win_rate'], player['country']))

#         return changed_lst

#     def selection_sort(self):
#         start_time = time.time()
#         for i in range(len(self.lst_players)):
#             min_index = i
#             for j in range(i + 1, len(self.lst_players)):
#                 self.stats["comparisons"] += 1
#                 if self.compare(self.lst_players[j], self.lst_players[min_index]):
#                     min_index = j
#             self.swap(i, min_index)
#         time_taken = time.time() - start_time
#         self.visual("Selection Sort", self.original, self.lst_players, time_taken)

#     def bubble_sort(self):
#         start_time = time.time()
#         for i in range(len(self.lst_players) - 1):
#             swapped = False
#             for j in range(len(self.lst_players) - 1 - i):
#                 self.stats["comparisons"] += 1
#                 if self.compare(self.lst_players[j + 1], self.lst_players[j]):
#                     self.swap(j, j + 1)
#                     swapped = True
#             if not swapped:
#                 break
#         time_taken = time.time() - start_time
#         self.visual.complete("Bubble Sort", self.original, self.lst_players, time_taken)

#     def compare(self, player1: Player, player2: Player) -> bool:
#         if player1.score != player2.score:
#             return player1.score > player2.score
#         if player1.win_rate != player2.win_rate:
#             return player1.win_rate > player2.win_rate
#         return player1.username < player2.username

#     def swap(self, i: int, j: int):
#         if i != j:
#             self.stats["swaps"] += 1
#             self.visual.before_swap(self.stats["steps"], self.lst_players, f"Swapping indices {i} and {j}", indices=[i, j])
#             self.lst_players[i], self.lst_players[j] = self.lst_players[j], self.lst_players[i]
#             self.stats["steps"] += 1

    # def selection_sort(self) -> List[Player]:
    #     if len(self.lst_players) <= 0:
    #         print("len student == 0.")
    #         return self.lst_players

    #     print("=" * 100)
    #     print("Selection Sort Process:")
    #     start: float = time.time()
    #     for i in range(len(self.lst_players)):
    #         currentDex: int = i
    #         for j in range(i + 1, len(self.lst_players)):
    #             if self.do_compare('score', self.lst_players[j], self.lst_players[currentDex]):
    #                 self.stats['comparisons'] += 1
    #                 currentDex = j

    #         self.do_swap(i, currentDex)
    #         self.stats['steps'] += 1
    
    #     end: float = time.time()
    #     self.visual.complete('Selection Sort', self.original, self.lst_players, end - start)
    #     return self.lst_players

    # def bubble_sort(self) -> List[Player]:
    #     if len(self.lst_players) <= 0:
    #         print("len student = 0.")
    #         return self.lst_players

    #     print("=" * 100)
    #     print("Bubble Sort Process:")
    #     m: int = len(self.lst_players)
    #     start: float = time.time()
    #     for i in range(m):
    #         is_swapped: bool = False
    #         for j in range(m - 1 - i):
    #             # Show current steps
    #             self.stats['comparisons'] += 1

    #             if self.do_compare('score', self.lst_players[j], self.lst_players[j + 1]):
    #                 self.do_swap(j, j + 1)

    #         if not is_swapped:
    #             break

    #     end = time.time()
    #     self.visual.complete("Bubble Sort", self.original, self.lst_players, end - start)
    #     return self.lst_players

    # def do_compare(self, sort_by: str, player1: Player, player2: Player) -> bool:
    #     if sort_by.lower() == 'score':
    #         p1_val: int = player1.score
    #         p2_val: int = player2.score
    #         if self.is_equal(p1_val, p2_val):
    #             return self.do_compare('win_rate', player1, player2)
    #         return self.compairing(p1_val, p2_val)

    #     elif sort_by.lower() == 'win_rate':
    #         p1_val: float = player1.win_rate
    #         p2_val: float = player2.win_rate
    #         if self.is_equal(p1_val, p2_val):
    #             return self.do_compare('username', player1, player2)
    #         return self.compairing(p1_val, p2_val)

    #     elif sort_by.lower() == 'username':
    #         p1_val: str = player1.username
    #         p2_val: str = player2.username
    #         return self.compairing(p1_val, p2_val)
    #     else:
    #         return False

    # def compairing(self, p1_value: int | float | str, p2_value: int | float | str) -> bool:
    #     return p2_value > p1_value

    # def is_equal(self, val1: int | float | str, val2: int | float | str) -> bool:
    #     return val1 == val2

    # def do_swap(self, i: int, currentDex: int) -> bool:
    #     if currentDex != i:
    #         self.visual.before_swap(self.stats['steps'], self.lst_players, 'Swap', i, currentDex, True)
    #         temp: Player = self.lst_players[i]
    #         self.lst_players[i] = self.lst_players[currentDex]
    #         self.lst_players[currentDex] = temp
    #         self.stats['swaps'] += 1
    #         self.visual.after_swap(self.lst_players, True)
    #     else:
    #         self.visual.before_swap(self.stats['steps'], self.lst_players, 'No Swap', i, currentDex, False)
    #         self.visual.after_swap(self.lst_players, False)