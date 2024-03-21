#include <string>
#include "grid/grid.hpp"
#include "AI.h"

PatternList goal2_4 { {"22220", 0.4}, {"22202", 0.4}, {"22022", 0.4}, {"20222", 0.4}, {"02222", 0.4}};
PatternList goal2_3 { {"22200", 0.3}, {"22020", 0.3}, {"22002", 0.3}, {"20220", 0.3}, {"20202", 0.3},
                      {"20022", 0.3}, {"02220", 0.3}, {"02202", 0.3}, {"02022", 0.3}, {"00222", 0.3}};
PatternList goal2_2 { {"22000", 0.2}, {"20200", 0.2}, {"20020", 0.2}, {"20002", 0.2}, {"02200", 0.2},
                      {"02020", 0.2}, {"02002", 0.2}, {"00220", 0.2}, {"00202", 0.2}, {"00022", 0.2}};

PatternList goal1_4 { {"11110", 0.4}, {"11101", 0.4}, {"11011", 0.4}, {"10111", 0.4}, {"01111", 0.4}};
PatternList goal1_3 { {"11100", 0.3}, {"11010", 0.3}, {"11001", 0.3}, {"10110", 0.3}, {"10101", 0.3},
                      {"10011", 0.3}, {"01110", 0.3}, {"01101", 0.3}, {"01011", 0.3}, {"00111", 0.3}};
PatternList goal1_2 { {"11000", 0.2}, {"10100", 0.2}, {"10010", 0.2}, {"10001", 0.2}, {"01100", 0.2},
                      {"01010", 0.2}, {"01001", 0.2}, {"00110", 0.2}, {"00101", 0.2}, {"00011", 0.2}};

PatternList block2_4 { {"22221", 3.8}, {"22212", 3.8}, {"22122", 3.8}, {"21222", 3.8}, {"12222", 3.8}};
PatternList block2_3 { {"22201", 2.6}, {"22021", 2.6}, {"22102", 2.6}, {"20221", 2.6}, {"20212", 2.6},
                      {"21022", 2.6}, {"12220", 2.6}, {"12202", 2.6}, {"12022", 2.6}, {"10222", 2.6},
                      {"22210", 2.6}, {"22120", 2.6}, {"22012", 2.6}, {"21220", 2.6}, {"21202", 2.6},
                      {"20122", 2.6}, {"02221", 2.6}, {"02212", 2.6}, {"02122", 2.6}, {"01222", 2.6}};
PatternList block2_2 { {"22001", 1.4}, {"20201", 1.4}, {"20021", 1.4}, {"20012", 1.4}, {"02201", 1.4},
                      {"02021", 1.4}, {"02012", 1.4}, {"00221", 1.4}, {"00212", 1.4}, {"00122", 1.4},
                      {"22010", 1.4}, {"20210", 1.4}, {"20120", 1.4}, {"20102", 1.4}, {"02210", 1.4},
                      {"02120", 1.4}, {"02102", 1.4}, {"01220", 1.4}, {"01202", 1.4}, {"01022", 1.4},
                      {"22100", 1.4}, {"21200", 1.4}, {"21020", 1.4}, {"21002", 1.4}, {"12200", 1.4},
                      {"12020", 1.4}, {"12002", 1.4}, {"10220", 1.4}, {"10202", 1.4}, {"10022", 1.4}};

PatternList block1_4 { {"11112", 1.8}, {"11121", 1.8}, {"11211", 1.8}, {"12111", 1.8}, {"21111", 1.8}};
PatternList block1_3 { {"11102", 1.6}, {"11012", 1.6}, {"11021", 1.6}, {"10112", 1.6}, {"10121", 1.6},
                      {"10211", 1.6}, {"01112", 1.6}, {"01121", 1.6}, {"01211", 1.6}, {"02111", 1.6},
                      {"11120", 1.6}, {"11210", 1.6}, {"11201", 1.6}, {"12110", 1.6}, {"12101", 1.6},
                      {"12011", 1.6}, {"21110", 1.6}, {"21101", 1.6}, {"21011", 1.6}, {"20111", 1.6}};
PatternList block1_2 { {"11002", 0.4}, {"10102", 0.4}, {"10012", 0.4}, {"10021", 0.4}, {"01102", 0.4},
                      {"01012", 0.4}, {"01021", 0.4}, {"00112", 0.4}, {"00121", 0.4}, {"00211", 0.4},
                      {"11020", 0.4}, {"10120", 0.4}, {"10210", 0.4}, {"10201", 0.4}, {"01120", 0.4},
                      {"01210", 0.4}, {"01201", 0.4}, {"02110", 0.4}, {"02101", 0.4}, {"02011", 0.4},
                      {"11200", 0.4}, {"12100", 0.4}, {"12010", 0.4}, {"12001", 0.4}, {"21100", 0.4},
                      {"21010", 0.4}, {"21001", 0.4}, {"20110", 0.4}, {"20101", 0.4}, {"20011", 0.4}};



float matching_cases(Grid& grid, int x, int y, char player, char opponent, int size, int line_size, int* lens, bool block) {
    int default_lens[3] = {0, 3, 4}; // C'est 2,3,4 dans ta doc de fonction mais dans ton code python tu as 3, 4 donc regarde bien pk
    float count = 0;
    PatternList goals;
    (void)opponent;
    (void)line_size;
    if (!lens)
        lens = default_lens;

    for (int i = 0; i < 3; i++) {
        if (lens[i] == 2) {
            if (player == '2') {
                goals.insert(goals.end(), goal2_2.begin(), goal2_2.end());
                if (block)
                    goals.insert(goals.end(), block1_2.begin(), block1_2.end());
            } else {
                goals.insert(goals.end(), goal1_2.begin(), goal1_2.end());
                goals.insert(goals.end(), block2_2.begin(), block2_2.end());
            }
        } else if (lens[i] == 3) {
            if (player == '2') {
                goals.insert(goals.end(), goal2_3.begin(), goal2_3.end());
                if (block)
                    goals.insert(goals.end(), block1_3.begin(), block1_3.end());
            } else {
                std::cout << "p1 3\n";
                goals.insert(goals.end(), goal1_3.begin(), goal1_3.end());
                if (block)
                    goals.insert(goals.end(), block2_3.begin(), block2_3.end());
            }
        } else if (lens[i] == 4) {
            if (player == '2') {
                goals.insert(goals.end(), goal2_4.begin(), goal2_4.end());
                if (block)
                    goals.insert(goals.end(), block1_4.begin(), block1_4.end());
            } else {
                goals.insert(goals.end(), goal1_4.begin(), goal1_4.end());
                if (block)
                    goals.insert(goals.end(), block2_4.begin(), block2_4.end());
            }
        }
    }
    count += __check_row(y, x, goals, grid, size);
    count += __check_column(y, x, goals, grid, size);
    count += __check_diagonal1(y, x, goals, grid, size);
    count += __check_diagonal2(y, x, goals, grid, size);
    return count;
}

/**
 * Count the number of substring in a string.
 * @param str
 * @param sub
 * @return
 */
int countSubstring(const std::string& str, const std::string& sub) {
    if (sub.length() == 0) return 0;
    int count = 0;
    for (size_t offset = str.find(sub); offset != std::string::npos; offset = str.find(sub, offset + sub.length())) {
        ++count;
    }
    return count;
}

/**
 * Check if the next move is winning by aligning five stones or more in a column.
 * @param row
 * @param col
 * @param goals
 * @param grid
 * @param size
 * @return
 */
float __check_column(int row, int col, PatternList goals, Grid grid, int size) {
    float cnt = 0;
    std::string col_g;
    for (int i = 0; i < size; i++) {
        col_g += grid.grid[col + (i * size)];
    }
    int start = std::max(0, row - 4);
    int end = std::min(size, row + 5);
    col_g = col_g.substr(start, end - start);
    for (const auto& goal : goals) {
        cnt += countSubstring(col_g, goal.first) * goal.second;
    }
    return cnt;
}

/**
 * Check if the next move is winning by aligning five stones or more in a row.
 * @param row
 * @param col
 * @param goals
 * @param grid
 * @param size
 * @return
 */
float __check_row(int row, int col, PatternList goals, Grid grid, int size) {
    float cnt = 0;
    std::string row_g;
    for (int i = 0; i < size; i++) {
        row_g += grid.grid[i + (row * size)];
    }
    int start = std::max(0, col - 4);
    int end = std::min(size, col + 5);
    row_g = row_g.substr(start, end - start);
    for (const auto& goal : goals) {
        cnt += countSubstring(row_g, goal.first) * goal.second;
    }
    return cnt;
}

/**
 * Check if the next move is winning by aligning five stones or more in a diagonal.
 * @param row y pos
 * @param col x pos
 * @param goals goal line
 * @param grid grid to analyse
 * @param size grid size
 * @return bool true or false
 */
float __check_diagonal1(int row, int col, PatternList goals, Grid grid, int size) {
    while (0 <= row && row < size && 0 <= col && col < size) {
        row--;
        col--;
    }
    row++;
    col++;
    std::string diag1_g;
    for (int i = 0; i < std::min(size - row, size - col); i++) {
        diag1_g += grid.grid[(row + i) * size + col + i];
    }
    int len_diag1_g = diag1_g.size();
    int start = std::max(0, std::min(col, row) - 4);
    int end = std::min(len_diag1_g, std::min(col, row) + 5);
    diag1_g = diag1_g.substr(start, end - start);
    float cnt = 0;
    for (const auto& goal : goals) {
        cnt += countSubstring(diag1_g, goal.first) * goal.second;
    }
    return cnt;
}

/**
 * Check if the next move is winning by aligning five stones or more in a diagonal.
 * @param row y pos
 * @param col x pos
 * @param goals goal line
 * @param grid grid to analyse
 * @param size grid size
 * @return bool true or false
 */
float __check_diagonal2(int row, int col, PatternList goals, Grid grid, int size) {
    while (0 <= row && row < size && 0 <= col && col < size) {
        row++;
        col--;
    }
    row--;
    col++;
    std::string diag2_g;
    for (int i = 0; i < std::min(row + 1, size - col); i++) {
        diag2_g += grid.grid[(row - i) * size + col + i];
    }
    int len_diag2_g = diag2_g.size();
    int start = std::max(0, std::min(col, len_diag2_g - row) - 4);
    int end = std::min(len_diag2_g, std::min(len_diag2_g - col, row) + 5);
    diag2_g = diag2_g.substr(start, end - start);
    float cnt = 0;
    for (const auto& goal : goals) {
        cnt += countSubstring(diag2_g, goal.first) * goal.second;
    }
    return cnt;
}
