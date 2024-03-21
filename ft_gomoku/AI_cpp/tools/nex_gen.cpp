#include "../AI.h"

std::vector<Grid> next_gen(Grid& grid, char &player, char &opponent,
						   std::vector<std::function<bool(int, int, char, Grid)>>& rules);
std::vector<std::tuple<int, int>> cluster(Grid &grid, char &player, char &opponent, int bypass);
void expend_cluster(std::vector<std::tuple<int, int>>& cluster, int i, int end, Grid& grid, char player, char opponent, int bypass);
bool can_expend(Grid& grid, int i, int x, int y, int x_exp, int y_exp, char player, char opponent, int bypass);
bool have_friends(Grid &grid, int x, int y, char player);


std::vector<Grid> next_gen(Grid& grid, char &player, char &opponent,
                           std::vector<std::function<bool(int, int, char, Grid)>>& rules) {
    std::vector<Grid> next_gen;
    std::vector<std::tuple<int, int>> cluster_c;
	int x;
	int y;

    cluster_c = cluster(grid, player, opponent, 0);

	for (std::tuple<int, int> c : cluster_c) {
		std::cout << "cluster_c: " << std::get<0>(c) << " " << std::get<1>(c) << std::endl;
		x = std::get<0>(c);
		y = std::get<1>(c);
		if ( 0 <= x && x < grid.size && 0 <= y && y < grid.size && grid.grid[x + y * grid.size] == '0'){
			Grid tmp = grid;
			if (tmp.add_rock(x, y, player, rules))
				next_gen.push_back(tmp);
		}
	}
    return next_gen;
}


std::vector<std::tuple<int, int>> cluster(Grid &grid, char &player, char &opponent, int bypass) {
    std::vector<std::tuple<int, int>> cluster;

    std::size_t first_p1;
    std::size_t first_p2;
    std::size_t last_p1;
    std::size_t last_p2;

    int tmp_p1_f = grid.size * grid.size;
    int tmp_p2_f = grid.size * grid.size;
    int tmp_p1_l = 0;
    int tmp_p2_l = 0;

    int i;
    int end;
	std::string tmp = grid.grid;

	std::cout << "p1 : " << player << " p2 : " << opponent << std::endl;

    first_p1 = tmp.find(player);
	std::cout << "first_p1: " << first_p1 << std::endl;
    first_p2 = tmp.find(opponent);
	std::cout << "first_p2: " << first_p2 << std::endl;
    last_p1 = tmp.rfind(player);
	std::cout << "last_p1: " << last_p1 << std::endl;
    last_p2 = tmp.rfind(opponent);
	std::cout << "last_p2: " << last_p2 << std::endl;


    if (first_p1 != std::string::npos)
        tmp_p1_f = first_p1;
    if (first_p2 != std::string::npos)
        tmp_p2_f = first_p2;
    if (last_p1 != std::string::npos)
        tmp_p1_l = last_p1;
    if (last_p2 != std::string::npos)
        tmp_p2_l = last_p2;

    i = std::min(tmp_p1_f, tmp_p2_f);
    i = std::max(i, 0);
    end = std::max(tmp_p1_l, tmp_p2_l);
    end = std::min(end, grid.size * grid.size);

    expend_cluster(cluster, i, end, grid, player, opponent, bypass);
    if (cluster.size() == 0) {
		expend_cluster(cluster, i, end, grid, player, opponent, 1);
	}
	if (cluster.size() == 0) {
		cluster.push_back(std::tuple<int, int>(grid.size / 2, grid.size / 2));
	}
    return cluster;
}


void expend_cluster(std::vector<std::tuple<int, int>>& cluster, int i, int end, Grid& grid, char player, char opponent, int bypass) {
    int x = 0;
    int y = 0;
    int _up = 0;
    int _down = 0;
    int _left = 0;
    int _right = 0;
	std::tuple<int, int> test;
    std::cout << "i: " << i << " end: " << end << std::endl;
    while (i < end) {
        x = i % grid.size;
        y = i / grid.size;
        if (grid.grid[i] != '0') {
			std::cout << "grid[i]: " << grid.grid[i] << std::endl;
            _up = y - 1;
            _down = y + 1;
            _left = x - 1;
            _right = x + 1;
            if (can_expend( grid, i, x, y, _left, _up,  player, opponent, bypass)){
				test = std::tuple<int, int>(_left, _up);
				if (std::find(cluster.begin(), cluster.end(), test) == cluster.end())
					cluster.push_back(test);
			}
            //up mid
            if (can_expend( grid, i, x, y, x, _up,  player, opponent, bypass)){
				test = std::tuple<int, int>(x, _up);
				if (std::find(cluster.begin(), cluster.end(), test) == cluster.end())
					cluster.push_back(test);
			}
            //up right
            if (can_expend( grid, i, x, y, _right, _up,  player, opponent, bypass)){
				test = std::tuple<int, int>(_right, _up);
				if (std::find(cluster.begin(), cluster.end(), test) == cluster.end())
					cluster.push_back(test);
			}
            //mid left
            if (can_expend( grid, i, x, y, _left, y,  player, opponent, bypass)){
				test = std::tuple<int, int>(_left, y);
				if (std::find(cluster.begin(), cluster.end(), test) == cluster.end())
					cluster.push_back(test);
			}
            //mid right
            if (can_expend( grid, i, x, y, _right, y,  player, opponent, bypass)){
				test = std::tuple<int, int>(_right, y);
				if (std::find(cluster.begin(), cluster.end(), test) == cluster.end())
					cluster.push_back(test);
			}
            //down left
            if (can_expend( grid, i, x, y, _left, _down, player, opponent, bypass)){
				test = std::tuple<int, int>(_left, _down);
				if (std::find(cluster.begin(), cluster.end(), test) == cluster.end())
					cluster.push_back(test);
			}
            //down mid
            if (can_expend( grid, i, x, y, x, _down, player, opponent, bypass)){
				test = std::tuple<int, int>(x, _down);
				if (std::find(cluster.begin(), cluster.end(), test) == cluster.end())
					cluster.push_back(test);
			}
            //down right
            if (can_expend( grid, i, x, y, _right, _down, player, opponent, bypass)){
				test = std::tuple<int, int>(_right, _down);
				if (std::find(cluster.begin(), cluster.end(), test) == cluster.end())
					cluster.push_back(test);
			}
        }
        i++;
    }
	std::cout << "cluster size: " << cluster.size() << std::endl;
}


bool can_expend(Grid& grid, int i, int x, int y, int x_exp, int y_exp, char player, char opponent, int bypass) {
    int prev_x;
    int prev_y;
	int prev_x2;
	int prev_y2;
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
        if ( 0 <= x_exp && x_exp < grid.size && 0 <= y_exp && y_exp < grid.size && grid.grid[x_exp + y_exp * grid.size] == '0') {
            if (bypass == 1 && x == grid.size / 2 && y == grid.size / 2)
                return true;
            prev_x = x - (x_exp - x);
            prev_y = y - (y_exp - y);
			if (0 <= prev_x && prev_x < grid.size && 0 <= prev_y && prev_y < grid.size &&
				grid.grid[prev_x + prev_y * grid.size] == opponent) {
				prev_x2 = x - 2 * (x_exp - x);
				prev_y2 = y - 2 * (y_exp - y);
				if (bypass != 0) {
					if (0 <= prev_x2 && prev_x2 < grid.size && 0 <= prev_y2 && prev_y2 < grid.size &&
						grid.grid[prev_x2 + prev_y2 * grid.size] == opponent)
						return true;
				} else {
					return true;
				}
			}
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