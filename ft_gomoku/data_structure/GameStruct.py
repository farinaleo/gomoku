import random
from dataclasses import dataclass
from ft_gomoku.grid.grid import Grid


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
		print("Player turn", self.player_turn)

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
