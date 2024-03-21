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
    int chosen_x = 0;
    int chosen_y = 0;

    PatternList block1_2 { {"11002", 0.4}, {"10102", 0.4}, {"10012", 0.4}, {"10021", 0.4}, {"01102", 0.4},
                           {"01012", 0.4}, {"01021", 0.4}, {"00112", 0.4}, {"00121", 0.4}, {"00211", 0.4},
                           {"11020", 0.4}, {"10120", 0.4}, {"10210", 0.4}, {"10201", 0.4}, {"01120", 0.4},
                           {"01210", 0.4}, {"01201", 0.4}, {"02110", 0.4}, {"02101", 0.4}, {"02011", 0.4},
                           {"11200", 0.4}, {"12100", 0.4}, {"12010", 0.4}, {"12001", 0.4}, {"21100", 0.4},
                           {"21010", 0.4}, {"21001", 0.4}, {"20110", 0.4}, {"20101", 0.4}, {"20011", 0.4}};

    Grid cpp_grid = Grid(grid, history, 19, ai_value, opponent_value);
//    int depth = 11;
//    int priority = 0;
    int result = check_diagonal2(4, 2, block1_2, cpp_grid, 19);
    std::cout << "Result: " << result << std::endl;
    std::cout << "Prio: " << get_priority(cpp_grid, ai_value, opponent_value) << std::endl;

    // Je suis a matching_cases.cpp, je fais la fonction get_priority. Il manque matching_cases pour finir get_priority.
    return (chosen_x + chosen_y * cpp_grid.size); // return the index in the line (easier to passer data between C++ and python)
}
