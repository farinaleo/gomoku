#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/19/24 6:40 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.
import ctypes
import time

import ft_gomoku


def convert_history(history_to_convert: []) -> str:
    return ':'.join('{}:{}:{}'.format(*move) for move in history_to_convert)


start_time = time.time()

lib = ctypes.CDLL("./ft_gomoku/AI_cpp/ft_gomoku_ai.so")
lib.run_ai.restype = ctypes.c_int
lib.run_ai.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char, ctypes.c_char]

# TEST
grid = ft_gomoku.Grid(19, '1', '2')
history = [('1', 0, 0), ('2', 1, 0), ('1', 0, 1), ('2', 1, 1), ('1', 2, 1), ('2', 1, 2), ('1', 2, 2), ('2', 3, 2), ('1', 2, 3), ('2', 3, 3), ('1', 4, 3), ('2', 3, 4), ('1', 4, 14), ('2', 5, 4), ('1', 4, 5), ('2', 15, 5),  ('1', 6, 5), ('2', 5, 6), ('1', 16, 6)]
history_str = convert_history(history)
print(history_str)
grid.add_rock(2, 2, '1', [])
grid.add_rock(3, 3, '1', [])
grid.add_rock(4, 4, '1', [])
grid.add_rock(5, 1, '1', [])
grid.add_rock(5, 2, '1', [])
grid.add_rock(5, 5, '2', [])
grid.add_rock(6, 6, '2', [])
grid.add_rock(7, 7, '2', [])
grid.add_rock(8, 8, '1', [])
grid.add_rock(18, 18, '2', [])

#print the grid with backslashes to see the grid
for i in range(19):
    print(grid.line_grid[i*19:(i+1)*19])

grid_string = ''.join(grid.line_grid)
bytes_history = (history_str + '\0').encode('utf-8')
bytes_grid = (grid_string + '\0').encode('utf-8')
print(bytes_grid)
print(bytes_history)
c_history = ctypes.c_char_p(bytes_history)
c_grid = ctypes.c_char_p(bytes_grid)

p1 = b'1'
p2 = b'2'

from ft_gomoku.AI.priority.priority import get_priority

print("PYTHONget priority", get_priority(grid, p1, p2))

result = lib.run_ai(c_grid, c_history, p1, p2)
execution_time_ms = (time.time() - start_time) * 1000

print("Execution time for run_ai :", execution_time_ms, "ms", "In case of > 500 ms, sorry leo, we are in a big trouble.")
print("Result:", result)
