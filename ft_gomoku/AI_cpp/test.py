#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/19/24 6:40 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.
import ctypes
import ft_gomoku

# Charge la bibliothèque partagée
lib = ctypes.CDLL("./ft_gomoku_ai.so")

# Définit le type de retour de la fonction
lib.run_ai.restype = ctypes.c_int  # Assumant que add_rock renvoie un int

# Définit les types d'arguments de la fonction
lib.run_ai.argtypes = [ctypes.c_char, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]  # Adapter les types selon la définition de la fonction

# Exemple d'appel de la fonction
row = 0
col = 0
grid = ft_gomoku.Grid(19, '1', '2')
grid.add_rock(1, 1, '1', [])
grid.add_rock(1, 2, '1', [])
grid.add_rock(1, 3, '1', [])
grid.add_rock(1, 4, '1', [])
grid.add_rock(1, 5, '1', [])

python_string = ''.join(grid.line_grid)
bytes_string = python_string.encode('utf-8')
print(bytes_string)

# Convertit en un pointeur de chaîne de caractères C
c_string = ctypes.c_char_p(bytes_string)

player = b'1'  # Assumant que player est une chaîne de caractères bytes
result = lib.run_ai(player, row, col, c_string)
print("Result:", result)
