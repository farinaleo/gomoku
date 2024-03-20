#include "grid.hpp"


Grid::Grid(const char *grid, const char *history, int size, char player1, char player2) {
    this->size = size;
    this->player1 = player1;
    this->player2 = player2;
    for (int i = 0; grid[i]; i++) {
        this->grid[i] = grid[i];
    }
    for (int i = 0; history[i]; i += 6) {
        if (!history[i] || !history[i + 2] || !history[i + 4])
            break;
        char player = history[i];
        int x = history[i + 2] - '0';
        if (history[i + 3] && history[i + 3] != ':') {
            x = (x * 10) + (history[i + 3] - '0');
            i++;
        }
        int y = history[i + 4] - '0';
        if (history[i + 5] && history[i + 5] != ':') {
            y = y * 10 + history[i + 5] - '0';
            i++;
        }
        this->history.push_back(std::make_tuple(player, x, y));
    }
    // print all tuples in history
//    for (int i = 0; i < static_cast<int>(this->history.size()); i++) {
//        std::cout << std::get<0>(this->history[i]) << ", " << std::get<1>(this->history[i]) << ", " << std::get<2>(this->history[i]) << std::endl;
//    }
//    this->grid[361] = '\0';
}

Grid::~Grid() {
    // Destructor
}

Grid::Grid(const Grid& arg) {
    // Copy constructor
    this->size = arg.size;
    this->player1 = arg.player1;
    this->player2 = arg.player2;
    for (int i = 0; i < 361; i++) {
        this->grid[i] = arg.grid[i];
    }
    this->grid[361] = '\0';
//    this->captured_stones = arg.captured_stones;
}

//Grid& Grid::operator=(const Grid& arg) {
//    // Assignment operator
//    this->size = arg.size;
//    this->player1 = arg.player1;
//    this->player2 = arg.player2;
//    for (int i = 0; i < 361; i++) {
//        this->grid[i] = arg.grid[i];
//    }
//    this->grid[361] = '\0';
////    this->captured_stones = arg.captured_stones;
//    return *this;
//}
//
//Move Grid::get_last_move(char player, int i) {
//    // Get the last move of a player
//    Move default_mv;
//    default_mv.player = '0';
//    default_mv.x = -1;
//    default_mv.y = -1;
//    if (this->history.size() == 0) {
//        return default_mv;
//    }
//    for (int j = this->history.size() - 1; j >= 0; j--) {
//        if (this->history[j].player == player) {
//            if (i == 0) {
//                return this->history[j];
//            }
//            i--;
//        }
//    }
//    return default_mv;
//}
//
//void Grid::add_move(char player, int x, int y) {
//    Move tmp;
//    tmp.player = player;
//    tmp.x = x;
//    tmp.y = y;
//    if (this->grid[x + y * this->size] != '0') {
//        return;
//    }
//    this->grid[x + y * this->size] = player;
//    this->history.push_back(tmp);
//}
//
//int Grid::get_capture(char player) {
//    return this->captured_stones[player];
//}
//
//int Grid::add_rock(int x, int y, char player, std::vector<std::function<bool(int, int, char, Grid)>> rules) {
//    if (0 <= x && x <= this->size && 0 <= y  && y <= this->size && this->grid[x + y * this->size] == '0') {
//        Grid _tmp = *this;
//        _tmp.grid[x + y * _tmp.size] = player;
//        _tmp.add_move(player, x, y);
//        for (int i = 0; i < static_cast<int>(rules.size()); i++) {
//            int _rtn = rules[i](x, y, player, _tmp);
//            if (_rtn == 1) {
//                this->winning = true;
//                return 1;
//            } else {
//                return 0;
//            }
//        }
//        this->grid[x + y * this->size] = player;
//        this->add_move(player, x, y);
//        return 1;
//    }
//    return 0;
//}
//
//int Grid::remove_rock(int x, int y) {
//    if (0 <= x && x <= this->size && 0 <= y  && y <= this->size && this->grid[x + y * this->size] != '0') {
//        this->grid[x + y * this->size] = '0';
//        return 1;
//    }
//    return 0;
//}
//
//int Grid::fore_rock(int x, int y, char player) {
//    if (0 <= x && x <= this->size && 0 <= y  && y <= this->size && this->grid[x + y * this->size] == '0') {
//        this->grid[x + y * this->size] = player;
//        return 1;
//    }
//    return 0;
//}
//
//int Grid::cnt_capture(char player, int stones) {
//    this->captured_stones[player] += stones;
//    return 1;
//}
