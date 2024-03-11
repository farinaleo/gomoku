import random
from dataclasses import dataclass
from ft_gomoku.grid.grid import Grid
from ft_gomoku.engine.image_control import get_image


@dataclass
class GameStruct:
	def __init__(self, size: int, player1, player2):
		self.grid = Grid(size + 1, player1[0], player2[1])
		self.player_1 = (player1, '1')
		self.player_2 = (player2, '2')
		self.grid_size = size
		self.game_mode = None
		self.player_turn = None
		self.time = 0
		self.board = []
		self.last_move = [None, None, None]
		self.random_player_turn()
		self.rock_white_img = None
		self.rock_black_img = None
		self.rock_white_last_img = None
		self.rock_black_last_img = None
		print("Player turn", self.player_turn)

	def init_img(self, radius: int):
		self.rock_white_img = get_image('rocks_white.png', radius, radius)
		self.rock_black_img = get_image('rocks_black.png', radius, radius)
		self.rock_black_last_img = get_image('rocks_black_last.png', radius, radius)
		self.rock_white_last_img = get_image('rocks_white_last.png', radius, radius)

	def get_rocks_img(self, player: int, last: bool):
		if player == '1':
			return self.rock_white_last_img if last else self.rock_white_img
		else:
			return self.rock_black_last_img if last else self.rock_black_img

	def get_last_move(self):
		return self.last_move

	def set_last_move(self, last_move):
		self.last_move = last_move

	def add_square(self, square):
		self.board.append(square)

	def set_game_mode(self, game_mode):
		self.game_mode = game_mode

	def get_game_mode(self):
		return self.game_mode

	def set_player_turn(self, player_turn):
		self.player_turn = player_turn

	def update_player_turn(self):
		self.player_turn = self.player_2 if self.player_turn == self.player_1 else self.player_1

	def get_player_turn(self):
		return self.player_turn

	def set_time(self, time):
		self.time = time

	def update_time(self, time):
		self.time += time

	def get_time(self):
		return self.time

	def get_board_size(self):
		return self.grid_size

	def get_player(self, player: int):
		if player == 1:
			return self.player_1
		else:
			return self.player_2

	def random_player_turn(self):
		random_player = random.randint(1, 2)
		self.player_turn = self.player_1 if random_player == 1 else self.player_2