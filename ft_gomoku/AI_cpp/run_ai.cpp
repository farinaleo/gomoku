//  ------------------------------------------------------------------------------------------------------------------ #
//  contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
//  github : https://github.com/farinaleo                                                             ▀▀▄██►           |
//  date : 3/19/24 6:34 PM                                                                           ▀▀███►           |
//                                                                                                    ░▀███►░█►        |
//                                                                                                    ▒▄████▀▀         |
//  ------------------------------------------------------------------------------------------------------------------ #
// Copyright (c) 2024.

#include <string>
#include <iostream>
#include "grid/grid.hpp"
#include "run_ai.h"
#include <chrono>
#include <algorithm>

//grid: Grid, rules, ai_value='1', opponent_value='2'
extern "C" int run_ai(const char *grid, const char *history, char ai_value, char opponent_value) {
    (void)ai_value;
    (void)opponent_value;

    Grid cpp_grid = Grid(grid, history, 19, ai_value, opponent_value);
//    int depth = 11;
//    int priority = 0;
    std::cout << "Prio: " << get_priority(cpp_grid, ai_value, opponent_value) << std::endl;

    // Je suis a matching_cases.cpp, je fais la fonction get_priority. Il manque matching_cases pour finir get_priority.
    return 1;
}
