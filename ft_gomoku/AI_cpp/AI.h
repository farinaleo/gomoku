//  ------------------------------------------------------------------------------------------------------------------ #
//  contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
//  github : https://github.com/farinaleo                                                             ▀▀▄██►           |
//  date : 3/20/24 10:21 AM                                                                           ▀▀███►           |
//                                                                                                    ░▀███►░█►        |
//                                                                                                    ▒▄████▀▀         |
//  ------------------------------------------------------------------------------------------------------------------ #
// Copyright (c) 2024.

#ifndef GMK_AI_H
#define GMK_AI_H

#include "grid/grid.hpp"

int get_priority(Grid& grid, char ai_value, char opponent_value);
int ai_priority(Grid& grid, char ai_value, char opponent_value);

float matching_cases(char *line, Grid grid, int x, int y, char player, char opponent, int size, int line_size, int* lens, bool block = true);

#endif //GMK_AI_H
