#ifndef GRID_HPP
# define GRID_HPP

# include <iostream>
# include <string>
# include <vector>
# include <map>
# include <functional>

// move struc with a player and a position x y
struct Move {
    char player;
    int x;
    int y;
};


class Grid {
    public:
        char player1;
        char player2;
        char grid[362];
        int size;
        bool winning = false;
        std::map<char, int> captured_stones;
        std::vector<Move> history;

        Grid(int size, char player1, char player2);
        ~Grid();
        Grid(const Grid& arg);
        Grid& operator=(const Grid& arg);

        Move get_last_move(char player='0', int i = 0);
        void add_move(char player, int x, int y);
        int get_capture(char player);
        int add_rock(int x, int y, char player, std::vector<std::function<bool(int, int, char, Grid)>> rules);
        int remove_rock(int x, int y);
        int fore_rock(int x, int y, char player);
        int cnt_capture(char player, int stones);
};


#endif