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
#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>
#include <map>

typedef std::pair<std::string, double> MyPair;
typedef std::vector<MyPair> PatternList;

int     get_priority(Grid& grid, char ai_value, char opponent_value);
int     ai_priority(Grid& grid, char ai_value, char opponent_value);
int     opponent_priority(Grid& grid, char ai_value, char opponent_value);

float   matching_cases(Grid& grid, int x, int y, char player, char opponent, int size, int line_size, int* lens, bool block = true);
float     __check_diagonal2(int row, int col, PatternList goals, Grid grid, int size);
float     __check_diagonal1(int row, int col, PatternList goals, Grid grid, int size);
float     __check_column(int row, int col, PatternList goals, Grid grid, int size);
float     __check_row(int row, int col, PatternList goals, Grid grid, int size);

#endif //GMK_AI_H
