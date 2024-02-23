from gomoku import Grid


def test_1():
	grid = Grid(3)
	grid.add_rock(0, 0, 'a', [])
	assert grid.add_rock(0, 0, 'a', []) is False


def test_2():
	grid = Grid(3)
	res_tab = [['a', 0, 0], [0, 0, 0], [0, 0, 0]]
	grid.add_rock(0, 0, 'a', [])
	grid.add_rock(0, 0, 'q', [])
	assert grid.get_grid() == res_tab


def test_3():
	grid = Grid(3)
	assert grid.add_rock(3, 2, 'q', []) is False


def test_4():
	grid = Grid(3)
	assert grid.add_rock(2, -1, 'q', []) is False
	