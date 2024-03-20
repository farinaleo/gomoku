//  ------------------------------------------------------------------------------------------------------------------ #
//  contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
//  github : https://github.com/farinaleo                                                             ▀▀▄██►           |
//  date : 3/19/24 7:00 PM                                                                           ▀▀███►           |
//                                                                                                    ░▀███►░█►        |
//                                                                                                    ▒▄████▀▀         |
//  ------------------------------------------------------------------------------------------------------------------ #
// Copyright (c) 2024.

#ifdef __cplusplus
extern "C" {
#endif

#include "grid/grid.hpp"

int run_ai(const char *grid, const char *history, char ai_value, char opponent_value);
int get_priority(Grid& grid, char ai_value, char opponent_value);
int ai_priority(Grid& grid, char ai_value, char opponent_value);

#ifdef __cplusplus
}
#endif