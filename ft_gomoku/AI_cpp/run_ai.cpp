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
extern "C" int run_ai(const char *grid, char ai_value, char opponent_value) {
    (void)ai_value;
    (void)opponent_value;
    // En moyenne, le temps d'execution de ce constructeur est de 0.001 ms.
    Grid cpp_grid = Grid(grid, 19, ai_value, opponent_value);
//    int depth = 11;
//    int priority = 0;

    int i = 0;
    while(cpp_grid.grid[i]) {
        if ((i + 1) % 19 == 0) {
            std::cout << cpp_grid.grid[i] << std::endl;
        } else {
            std::cout << cpp_grid.grid[i] << ", ";
        }
        i++;
    }
    return 1;
}
