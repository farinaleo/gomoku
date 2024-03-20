#include <string>
#include <iostream>
#include "grid/grid.hpp"
#include "run_ai.h"

/**
 * @brief evaluate the priority according to the IA and opponent last moves.
 * @param grid the game.
 * @param ai_value the value associated with the AI.
 * @param opponent_value the value associated with the opponent.
 * @return (int) 2 if the IA has to block the opponent, 1 if the IA can win with one move, 0 otherwise.
 */
int get_priority(Grid& grid, char ai_value, char opponent_value) {
    (void)grid;
    (void)ai_value;
    (void)opponent_value;
    return ai_priority(grid, ai_value, opponent_value);
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
    (void)opponent_value;
    if (std::get<0>(ia_last_move) == '0')
        return 0;
    return 1;
}
