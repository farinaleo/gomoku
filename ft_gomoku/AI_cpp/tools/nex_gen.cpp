#include "../AI.h"

std::vector<Grid> next_gen(Grid& grid, char player, char opponent,
                           std::vector<std::function<bool(int, int, char, Grid)>> rules) {
    std::vector<Grid> next_gen;
    std::vector<Move> cluster;

    cluster = cluster()

    return next_gen;
}


std::vector<Move> cluster(Grid &grid, char player, char opponent) {
    std::vector<Move> cluster;

    char *first_p1;
    char *first_p2;
    char *last_p1;
    char *last_p2;

    int tmp_p1_f = grid.size * grid.size;
    int tmp_p2_f = grid.size * grid.size;
    int tmp_p1_l = 0;
    int tmp_p2_l = 0;

    int i;
    int end;

    first_p1 = std::find(std::begin(grid.grid), std::end(grid.grid), player);
    first_p2 = std::find(std::begin(grid.grid), std::end(grid.grid), opponent);
    last_p1 = std::find(std::rbegin(grid.grid), std::rend(grid.grid), player);
    last_p2 = std::find(std::rbegin(grid.grid), std::rend(grid.grid), opponent);

    if (first_p1 != std::end(grid.grid))
        tmp_p1_f = (first_p1 - grid.grid);
    if (first_p2 != std::end(grid.grid))
        tmp_p2_f = (first_p2 - grid.grid);
    if (last_p1 != std::rend(grid.grid))
        tmp_p1_l = (last_p1 - grid.grid);
    if last_p2 != std::rend(grid.grid))
        tmp_p2_l = (last_p2 - grid.grid);

    i = std::min(tmp_p1_f, tmp_p2_f);
    i = std::max(i, 0);
    end = std::max(tmp_p1_l, tmp_p2_l);
    end = std::min(end, grid.size * grid.size);

    return cluster;
}


void expend_cluster(std::vector<Move>& cluster, int i, int end, Grid& grid, char player, char opponent, int bypass) {
    int x = 0;
    int y = 0;
    int _up = 0;
    int _down = 0;
    int _left = 0;
    int _right = 0;
    
    while (i < end) {
        x = i % grid.size;
        y = i / grid.size;
        if (grid.grid[i] == '0') {
            _up = y - 1;
            _down = y + 1;
            _left = x - 1;
            _right = x + 1;
        }
        i++;
    }
}


bool can_expend(Grid& grid, int i, int x, int y, int x_exp, int y_exp, char player, char opponent, int bypass) {
    int prev_x;
    int prev_y;
    if (grid.grid[i] == player) {
        if (have_friends(grid, x, y, player)) {
            prev_x = x - (x_exp - x);
            prev_y = y - (y_exp - y);
            if (bypass != 0) {
                if (!(0 <= prev_x && prev_x < grid.size && 0 <= prev_y && prev_y < grid.size &&
                      grid.grid[prev_x + prev_y * grid.size] == player))
                    return false;
            }
            if (0 <= x_exp && x_exp < grid.size && 0 <= y_exp && y_exp < grid.size && grid.grid[x_exp + y_exp * grid.size] == '0')
                return true;
        }
    } else {
        if ( 0 <= _exp && x_exp < grid.size && 0 <= y_exp && y_exp < grid.size && grid.grid[x_exp + y_exp * grid.size] == '0') {
            if (bypass == 1 && x == grid.size / 2 && y == grid.size / 2)
                return true;
            prev_x = x - (x_exp - x);
            prev_y = y - (y_exp - y);
            if (bypass == 0) {
                if (0 <= prev_x && prev_x < grid.size && 0 <= prev_y && prev_y < grid.size &&
                    grid.grid[prev_x + prev_y * grid.size] == opponent)
                    return true;
            } else
                return true;
        }
    }
    return false;
}

bool have_friends(Grid &grid, int x, int y, char player) {
    if (0 <= x - 1 && x -1  < grid.size && 0 <= y - 1 && y - 1 < grid.size && grid.grid[(x - 1) + (y - 1) * grid.size] == player)
        return true;
    else if (0 <= x && x < grid.size && 0 <= y - 1 && y - 1 < grid.size && grid.grid[x + (y - 1) * grid.size] == player)
        return true;
    else if (0 <= x + 1 && x + 1 < grid.size && 0 <= y - 1 && y - 1 < grid.size && grid.grid[(x + 1) + (y - 1) * grid.size] == player)
        return true;
    else if (0 <= x - 1 && x - 1 < grid.size && 0 <= y && y - 1 < grid.size && grid.grid[(x - 1) + y * grid.size] == player)
        return true;
    else if (0 <= x + 1 && x + 1 < grid.size && 0 <= y && y < grid.size && grid.grid[(x + 1) + y * grid.size] == player)
        return true;
    else if (0 <= x - 1 && x - 1 < grid.size && 0 <= y + 1 && y + 1 < grid.size && grid.grid[(x - 1) + (y + 1) * grid.size] == player)
        return true;
    else if (0 <= x && x < grid.size && 0 <= y + 1 && y + 1< grid.size && grid.grid[x + (y + 1) * grid.size] == player)
        return true;
    else if (0 <= x + 1 && x + 1 < grid.size && 0 <= y + 1 && y + 1 < grid.size && grid.grid[(x + 1) + (y + 1) * grid.size] == player)
        return true;
    return false;
}