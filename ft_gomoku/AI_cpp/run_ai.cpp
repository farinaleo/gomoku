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

extern "C" int run_ai(char player, int x, int y,const char *groud) { // change decla to match with python func
    Grid tmp = Grid(19, '1', '2');
    std::cout << tmp.grid << std::endl;
    std::cout << groud << std::endl;
    int i = 0;
    while(groud[i]) {
        std::cout << groud[i] << ' ';
        tmp.grid[i] = groud[i];
        i++;
    }
    std::cout << tmp.grid << std::endl;
    tmp.add_move(player, x, y);
    tmp.add_rock(x + 1, y, player, {});
    std::cout << "AI move: " << player << " " << x << " " << y << std::endl;
    std::cout << tmp.grid << std::endl;
    return 1;
}
