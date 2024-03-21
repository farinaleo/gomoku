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
    int chosen_x = 0;
    int chosen_y = 0;

    Grid cpp_grid = Grid(grid, history, 19, ai_value, opponent_value);
//    int depth = 11;
//    int priority = 0;
    int result = get_priority(cpp_grid, ai_value, opponent_value);
    std::cout << "------------------------------------ CPP Result: " << result << std::endl;

    return (chosen_x + chosen_y * cpp_grid.size); // return the index in the line (easier to passer data between C++ and python)
}
