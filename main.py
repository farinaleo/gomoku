# from gomoku import SettingsStruct
#
# settings = SettingsStruct()
# settings.load()
# settings.print()
# settings.set_fps(20)
# settings.save()
import time

import gomoku as gmk

grid = gmk.Grid(19)
start = time.time()
grid.add_rock(8, 0, 'q', [gmk.five_to_win])
grid.add_rock(4, 0, 'q', [gmk.five_to_win])
grid.add_rock(3, 1, 'q', [gmk.five_to_win])
grid.add_rock(2, 2, 'q', [gmk.five_to_win])
grid.add_rock(1, 3, 'q', [gmk.five_to_win])
grid.add_rock(0, 4, 'q', [gmk.five_to_win])
for line in grid.get_grid():
	print(line)