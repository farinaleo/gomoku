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
lib = ctypes.CDLL("./ft_gomoku/AI_cpp/ft_gomoku_ai.so")

# Définit le type de retour de la fonction
lib.run_ai.restype = ctypes.c_int  # Assumant que add_rock renvoie un int

# Définit les types d'arguments de la fonction
lib.run_ai.argtypes = [ctypes.c_char_p, ctypes.c_char, ctypes.c_char]  # Adapter les types selon la définition de la fonction

# Exemple d'appel de la fonction
grid = ft_gomoku.Grid(19, '1', '2')
grid.add_rock(0, 0, '1', [])
grid.add_rock(9, 9, '2', [])

python_string = ''.join(grid.line_grid)
bytes_string = python_string.encode('utf-8')
print(bytes_string)

# Convertit en un pointeur de chaîne de caractères C
c_string = ctypes.c_char_p(bytes_string)

p1 = b'1'
p2 = b'2'
result = lib.run_ai(c_string, p1, p2)
print("Result:", result)
