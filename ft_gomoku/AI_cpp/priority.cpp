#include <string>
#include <iostream>
#include <cmath>
#include "grid/grid.hpp"
#include "AI.h"

/**
 * @brief evaluate the priority according to the IA and opponent last moves.
 * @param grid the game.
 * @param ai_value the value associated with the AI.
 * @param opponent_value the value associated with the opponent.
 * @return (int) 2 if the IA has to block the opponent, 1 if the IA can win with one move, 0 otherwise.
 */
int get_priority(Grid& grid, char ai_value, char opponent_value) {
    int priority = std::max(ai_priority(grid, ai_value, opponent_value), opponent_priority(grid, ai_value, opponent_value));
    return priority;
}

/**
 * @brief evaluate the AI priority according to its last move.
 * @param grid the game.
 * @param ai_value the value associated with the AI.
 * @param opponent_value the value associated with the opponent.
 * @return (int) the priority rate.
 */
int ai_priority(Grid& grid, char ai_value, char opponent_value) {
    std::tuple<char, int, int> ia_last_move = grid.get_last_move(ai_value);
    if (std::get<0>(ia_last_move) == '0')
        return 0;
    int lens[3] = {0, 3, 4};
    float p_4 = matching_cases(grid, std::get<1>(ia_last_move), std::get<2>(ia_last_move), ai_value, opponent_value, grid.size, pow(grid.size, 2), lens, false);
    std::cout << "CPP -- P4" << p_4 << std::endl;
    if (p_4 > 0)
        return 1;
    return 0;
}

/**
 * @brief evaluate the opponent priority according to its last move.
 * @param grid the game.
 * @param ai_value the value associated with the AI.
 * @param opponent_value the value associated with the opponent.
 * @return (int) the priority rate.
 */
int opponent_priority(Grid& grid, char ai_value, char opponent_value) {
    (void)ai_value;
    std::tuple<char, int, int> opponent_last_move = grid.get_last_move(opponent_value);
    if (std::get<0>(opponent_last_move) == '0')
        return 0;
    int lens[3] = {0, 3, 4};
    float p_4 = matching_cases(grid, std::get<1>(opponent_last_move), std::get<2>(opponent_last_move), opponent_value, ai_value, grid.size, pow(grid.size, 2), lens, false);
    if (p_4 > 0)
        return 2;
    return 0;
}
