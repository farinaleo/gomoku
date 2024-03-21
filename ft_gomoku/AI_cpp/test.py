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

#Load the shared library
lib = ctypes.CDLL("./ft_gomoku/AI_cpp/ft_gomoku_ai.so")

# Define the return type of the function
lib.run_ai.restype = ctypes.c_int

# Define the types of the function arguments
lib.run_ai.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char, ctypes.c_char]






block1_2 = [('22201', 2.6), ('22021', 2.6), ('22102', 2.6), ('20221', 2.6), ('20212', 2.6),
            ('21022', 2.6), ('12220', 2.6), ('12202', 2.6), ('12022', 2.6), ('10222', 2.6),
            ('22210', 2.6), ('22120', 2.6), ('22012', 2.6), ('21220', 2.6), ('21202', 2.6),
            ('20122', 2.6), ('02221', 2.6), ('02212', 2.6), ('02122', 2.6), ('01222', 2.6),
            ('22001', 1.4), ('20201', 1.4), ('20021', 1.4), ('20012', 1.4), ('02201', 1.4),
            ('02021', 1.4), ('02012', 1.4), ('00221', 1.4), ('00212', 1.4), ('00122', 1.4),
            ('22010', 1.4), ('20210', 1.4), ('20120', 1.4), ('20102', 1.4), ('02210', 1.4),
            ('02120', 1.4), ('02102', 1.4), ('01220', 1.4), ('01202', 1.4), ('01022', 1.4),
            ('22100', 1.4), ('21200', 1.4), ('21020', 1.4), ('21002', 1.4), ('12200', 1.4),
            ('12020', 1.4), ('12002', 1.4), ('10220', 1.4), ('10202', 1.4), ('10022', 1.4)]













# TEST
grid = ft_gomoku.Grid(19, '1', '2')
history = [('1', 0, 0), ('2', 1, 0), ('1', 0, 1), ('2', 1, 1), ('1', 2, 1), ('2', 1, 2), ('1', 2, 2), ('2', 3, 2), ('1', 2, 3), ('2', 3, 3), ('1', 4, 3), ('2', 3, 4), ('1', 4, 14), ('2', 5, 4), ('1', 4, 5), ('2', 15, 5),  ('1', 6, 5), ('2', 5, 6), ('1', 16, 6)]

history_str = convert_history(history)
print(history_str)
grid.add_rock(2, 2, '1', [])
grid.add_rock(3, 3, '1', [])
grid.add_rock(4, 4, '1', [])
grid.add_rock(5, 5, '2', [])
grid.add_rock(6, 6, '2', [])
grid.add_rock(7, 7, '2', [])
grid.add_rock(8, 8, '1', [])
grid.add_rock(18, 18, '2', [])

grid_string = ''.join(grid.line_grid)
bytes_history = (history_str + '\0').encode('utf-8')
bytes_grid = (grid_string + '\0').encode('utf-8')
print(bytes_grid)
print(bytes_history)
c_history = ctypes.c_char_p(bytes_history)
c_grid = ctypes.c_char_p(bytes_grid)

p1 = b'1'
p2 = b'2'

from ft_gomoku.AI.heurisitic.matching_cases import __check_diagonal2

print("check daig py:", __check_diagonal2(4, 2, block1_2, grid.line_grid, 19))

result = lib.run_ai(c_grid, c_history, p1, p2)
execution_time_ms = (time.time() - start_time) * 1000

print("Execution time for run_ai :", execution_time_ms, "ms", "In case of > 500 ms, sorry leo, we are in a big trouble.")
print("Result:", result)
